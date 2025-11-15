require_relative "boot"

require "rails/all"

Bundler.require(*Rails.groups)

module Autodialer
  class Application < Rails::Application
    config.load_defaults 7.0
    config.time_zone = 'UTC'
    config.active_record.default_timezone = :utc
  end
end

