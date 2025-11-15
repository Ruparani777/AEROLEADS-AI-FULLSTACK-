Twilio.configure do |config|
  config.account_sid = ENV['TWILIO_ACCOUNT_SID'] || 'your_account_sid_here'
  config.auth_token = ENV['TWILIO_AUTH_TOKEN'] || 'your_auth_token_here'
end

