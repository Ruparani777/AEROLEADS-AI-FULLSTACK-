class ProcessCallsJob < ApplicationJob
  queue_as :default
  
  def perform
    return unless Rails.cache.read('calls_running')
    
    pending_calls = Call.pending_or_queued.limit(1)
    
    pending_calls.each do |call|
      next unless Rails.cache.read('calls_running')
      
      call.update(status: :queued)
      make_twilio_call(call)
      
      # Wait a bit before processing next call (sequential calling)
      sleep(2)
    end
    
    # Schedule next batch if still running
    if Rails.cache.read('calls_running') && Call.pending_or_queued.exists?
      ProcessCallsJob.set(wait: 5.seconds).perform_later
    end
  end
  
  private
  
  def make_twilio_call(call)
    return unless Rails.env.production? || ENV['TWILIO_ACCOUNT_SID'].present?
    
    begin
      client = Twilio::REST::Client.new
      
      from_number = ENV['TWILIO_PHONE_NUMBER'] || '+15005550006'
      to_number = normalize_phone_number(call.number)
      
      # For testing: simulate calls
      if Rails.env.development? || ENV['TWILIO_TEST_MODE'] == 'true'
        call.update(
          status: [:completed, :failed, :no_answer, :busy].sample,
          started_at: Time.current,
          finished_at: Time.current + rand(10..60).seconds,
          twilio_sid: "test_#{SecureRandom.hex(10)}"
        )
        return
      end
      
      twilio_call = client.calls.create(
        to: to_number,
        from: from_number,
        url: "#{ENV['BASE_URL'] || 'http://localhost:3000'}/twiml/voice?call_id=#{call.id}",
        status_callback: "#{ENV['BASE_URL'] || 'http://localhost:3000'}/twiml/status",
        status_callback_event: ['initiated', 'ringing', 'answered', 'completed']
      )
      
      call.update(
        status: :ringing,
        twilio_sid: twilio_call.sid,
        started_at: Time.current
      )
    rescue => e
      Rails.logger.error "Twilio call error: #{e.message}"
      call.update(status: :failed, finished_at: Time.current)
    end
  end
  
  def normalize_phone_number(number)
    cleaned = number.gsub(/[^\d+]/, '')
    
    if cleaned.length == 10
      "+1#{cleaned}"
    elsif cleaned.length == 11 && cleaned.start_with?('1')
      "+#{cleaned}"
    elsif !cleaned.start_with?('+')
      "+#{cleaned}"
    else
      cleaned
    end
  end
end

