class CallsController < ApplicationController
  before_action :set_call, only: [:show, :update, :destroy]
  
  def index
    @calls = Call.recent.limit(100)
    render json: @calls
  end
  
  def show
    render json: @call
  end
  
  def create
    @call = Call.new(call_params)
    if @call.save
      render json: @call, status: :created
    else
      render json: @call.errors, status: :unprocessable_entity
    end
  end
  
  def upload_csv
    if params[:file].present?
      file = params[:file]
      numbers = []
      
      CSV.foreach(file.path, headers: false) do |row|
        number = row[0]&.strip
        numbers << number if number.present?
      end
      
      create_calls_from_numbers(numbers)
      render json: { message: "Uploaded #{numbers.count} numbers", count: numbers.count }
    else
      render json: { error: "No file provided" }, status: :unprocessable_entity
    end
  end
  
  def upload_textarea
    numbers_text = params[:numbers] || params['numbers'] || ""
    numbers = numbers_text.split(/[\n,;]/).map(&:strip).reject(&:empty?)
    
    create_calls_from_numbers(numbers)
    render json: { message: "Uploaded #{numbers.count} numbers", count: numbers.count }
  end
  
  def start_calls
    Rails.cache.write('calls_running', true)
    
    # Start background job to process calls
    ProcessCallsJob.perform_later
    
    render json: { message: "Calls started", status: "running" }
  end
  
  def stop_calls
    Rails.cache.write('calls_running', false)
    render json: { message: "Calls stopped", status: "stopped" }
  end
  
  def ai_prompt
    prompt = params[:prompt] || params['prompt'] || ""
    number = extract_phone_number(prompt)
    
    if number
      call = Call.create(number: number, status: :queued)
      make_twilio_call(call)
      render json: { message: "Call initiated to #{number}", call: call.as_json(only: [:id, :number, :status]) }
    else
      render json: { error: "Could not extract phone number from prompt" }, status: :unprocessable_entity
    end
  end
  
  def status
    @calls = Call.recent.limit(50)
    @is_running = Rails.cache.read('calls_running') || false
    @pending_count = Call.pending_or_queued.count
    
    render json: {
      calls: @calls.as_json(only: [:id, :number, :status, :started_at, :finished_at, :twilio_sid]),
      is_running: @is_running,
      pending_count: @pending_count
    }
  end
  
  private
  
  def set_call
    @call = Call.find(params[:id])
  end
  
  def call_params
    params.require(:call).permit(:number, :status, :twilio_sid)
  end
  
  def create_calls_from_numbers(numbers)
    numbers.each do |number|
      Call.create(number: number, status: :pending) unless Call.exists?(number: number, status: [:pending, :queued])
    end
  end
  
  def extract_phone_number(text)
    # Simple regex to extract phone numbers
    # Matches patterns like: 1800xxxxxx, 1-800-xxx-xxxx, +1 800 xxx xxxx, etc.
    patterns = [
      /\b(\+?1?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})\b/,
      /\b(\d{10,})\b/,
      /call\s+([\d\s\-\(\)\+]+)/i,
      /(\+?1?[-.\s]?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4})/
    ]
    
    patterns.each do |pattern|
      match = text.match(pattern)
      if match
        number = match[1] || match[0]
        # Clean up the number
        cleaned = number.gsub(/[\s\-\(\)\.]/, '')
        return cleaned if cleaned.length >= 10
      end
    end
    
    nil
  end
  
  def make_twilio_call(call)
    return unless Rails.env.production? || ENV['TWILIO_ACCOUNT_SID'].present?
    
    begin
      client = Twilio::REST::Client.new
      
      # Use a TwiML URL or Twilio Studio flow
      # For testing, use Twilio test credentials or trial account
      from_number = ENV['TWILIO_PHONE_NUMBER'] || '+15005550006' # Twilio test number
      to_number = normalize_phone_number(call.number)
      
      # For testing: don't call real numbers, use test numbers
      if Rails.env.development? || ENV['TWILIO_TEST_MODE'] == 'true'
        # Simulate call for testing
        call.update(
          status: :completed,
          started_at: Time.current,
          finished_at: Time.current + 30.seconds,
          twilio_sid: "test_#{SecureRandom.hex(10)}"
        )
        return
      end
      
      twilio_call = client.calls.create(
        to: to_number,
        from: from_number,
        url: twiml_url(call),
        status_callback: status_callback_url,
        status_callback_event: ['initiated', 'ringing', 'answered', 'completed']
      )
      
      call.update(
        status: :queued,
        twilio_sid: twilio_call.sid,
        started_at: Time.current
      )
    rescue => e
      Rails.logger.error "Twilio call error: #{e.message}"
      call.update(status: :failed, finished_at: Time.current)
    end
  end
  
  def normalize_phone_number(number)
    # Remove all non-digit characters except +
    cleaned = number.gsub(/[^\d+]/, '')
    
    # Add +1 if it's a 10-digit number
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
  
  def twiml_url(call)
    # This would be a URL to your TwiML response
    # For now, we'll use a simple TwiML response
    "#{request.base_url}/twiml/voice?call_id=#{call.id}"
  end
  
  def status_callback_url
    "#{request.base_url}/twiml/status"
  end
end

