Rails.application.routes.draw do
  root 'blog#index'
  
  resources :blog, only: [:index, :show, :new, :create, :edit, :update] do
    collection do
      post :generate_articles
      get :generation_log
    end
    member do
      patch :save_draft
    end
  end
end

