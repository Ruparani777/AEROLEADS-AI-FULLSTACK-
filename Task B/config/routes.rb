Rails.application.routes.draw do
  root 'home#index'
  
  resources :calls do
    collection do
      post :upload_csv
      post :upload_textarea
      post :start_calls
      post :stop_calls
      post :ai_prompt
      get :status
    end
  end
  
  # Twilio webhooks
  post '/twiml/voice', to: 'twiml#voice'
  post '/twiml/status', to: 'twiml#status'
end

