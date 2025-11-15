class TwimlController < ApplicationController
  skip_before_action :verify_authenticity_token
  
  def voice
    call = Call.find_by(id: params[:call_id])
    
    response = Twilio::TwiML::VoiceResponse.new do |r|
      r.say(message: "This is a test call from the autodialer system.", voice: 'alice')
      r.pause(length: 1)
      r.say(message: "Thank you for your time. Goodbye.", voice: 'alice')
      r.hangup
    end
    
    render xml: response.to_s
  end
  
  def status
    call_sid = params[:CallSid]
    call_status = params[:CallStatus]
    
    call = Call.find_by(twilio_sid: call_sid)
    
    if call
      case call_status
      when 'ringing', 'initiated'
        call.update(status: :ringing)
      when 'in-progress', 'answered'
        call.update(status: :in_progress)
      when 'completed'
        call.update(status: :completed, finished_at: Time.current)
      when 'busy'
        call.update(status: :busy, finished_at: Time.current)
      when 'no-answer'
        call.update(status: :no_answer, finished_at: Time.current)
      when 'failed', 'canceled'
        call.update(status: :failed, finished_at: Time.current)
      end
    end
    
    head :ok
  end
end

