class HomeController < ApplicationController
  def index
    @calls = Call.recent.limit(100)
    @pending_count = Call.pending_or_queued.count
    @is_running = Rails.cache.read('calls_running') || false
  end
end

