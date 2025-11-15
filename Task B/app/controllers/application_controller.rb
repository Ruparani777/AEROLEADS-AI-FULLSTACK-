class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
  
  before_action :parse_json_params, if: -> { request.content_type&.include?('application/json') }
  
  private
  
  def parse_json_params
    return unless request.body.size > 0
    
    body = request.body.read
    request.body.rewind
    
    begin
      json_params = JSON.parse(body)
      params.merge!(json_params)
    rescue JSON::ParserError
      # Ignore if JSON parsing fails
    end
  end
end

