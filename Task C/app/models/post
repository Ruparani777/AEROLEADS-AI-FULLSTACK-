class Post < ApplicationRecord
  validates :title, presence: true
  
  scope :published, -> { where(status: 'published') }
  scope :recent, -> { order(created_at: :desc) }
end

