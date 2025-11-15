# AEROLEADS-AI-FULLSTACK-

# 🚀 Project Exploration Summary

## Overview
Your workspace contains 3 complete projects demonstrating real-world Ruby on Rails and Python development:

---

## 1. 📱 **Autodialer** (Rails App)
**Purpose**: Automated phone call dialer using Twilio Voice API

### Key Features
- ✅ Web UI for uploading phone numbers (CSV or manual paste)
- ✅ Twilio Voice integration for outbound calls
- ✅ Call logs & status tracking
- ✅ Custom TTS scripts for call content
- ✅ Background job support (Sidekiq)

### Architecture
```
autodialer/
├── app/
│   ├── controllers/
│   │   ├── application_controller.rb
│   │   └── calls_controller.rb          # Handles call UI
│   ├── models/
│   │   ├── call_batch.rb               # Batch of calls to make
│   │   └── call_logs.rb                # Individual call records
│   ├── jobs/
│   │   └── trigger_call_batch_job.rb   # Background job
│   ├── services/
│   │   └── twilio_call_service.rb      # Twilio integration
│   └── views/
│       └── calls/
│           ├── index.html.erb          # Call logs page
│           └── new.html.erb            # New call form
├── config/
│   ├── routes.rb                       # Rails routes
│   ├── database.yml                    # DB config
│   └── application.rb                  # App config
└── db/
    └── migrate/
        ├── 001_create_call_batches.rb
        └── 002_create_call_logs.rb

```

### Setup Steps
```bash
cd autodialer
bundle install
# Configure .env with:
# - TWILIO_ACCOUNT_SID
# - TWILIO_AUTH_TOKEN
# - TWILIO_CALLER_ID
rails db:create db:migrate
rails server  # Starts at http://localhost:3000
```

### Tech Stack
- Ruby 3.2.9
- Rails 7.1
- PostgreSQL (configurable to SQLite)
- Twilio Ruby SDK
- Sidekiq (background jobs)
- Puma (app server)

---

## 2. 📝 **AI Blog Generator** (Rails Engine)
**Purpose**: Generate AI-written blog posts using LLM providers

### Key Features
- ✅ Supports multiple LLM providers (OpenAI, Gemini, Perplexity)
- ✅ Configurable blog topics (YAML)
- ✅ ArticlesController for viewing generated posts
- ✅ ActiveRecord storage for articles
- ✅ Mountable Rails engine (integrated into autodialer at `/blog`)

### Architecture
```
ai_blog_generator/
├── app/
│   ├── controllers/
│   │   └── ai_blog_generator/
│   │       └── articles_controller.rb  # List & show articles
│   ├── models/
│   │   └── ai_blog_generator/
│   │       ├── application_record.rb
│   │       └── article.rb              # Article model
│   ├── services/
│   │   └── ai/
│   │       ├── blog_generator.rb       # Main generator
│   │       ├── blog_provider_config.rb # Provider config
│   │       ├── gemini_client.rb        # Gemini API
│   │       ├── open_ai_client.rb       # OpenAI API
│   │       └── perplexity_client.rb    # Perplexity API
│   └── views/
│       └── ai_blog_generator/
│           └── articles/
│               ├── index.html.erb      # List articles
│               └── show.html.erb       # View article
├── config/
│   ├── routes.rb                       # Engine routes
│   └── blog_topics.yml                 # Article topics
├── db/
│   └── migrate/
│       └── 001_create_articles.rb
└── lib/
    ├── ai_blog_generator.rb
    └── ai_blog_generator/
        ├── engine.rb
        └── version.rb
```

### Setup Steps
```bash
cd ai_blog_generator
bundle install
# Configure .env with:
# - OPENAI_API_KEY  (or equivalent for provider)
# - GEMINI_API_KEY
# - PERPLEXITY_API_KEY
rails db:migrate
```

### Usage Example
```ruby
# In a Rails console or controller:
generator = Ai::BlogGenerator.new(provider: :openai)
titles = ["Rails 7 Best Practices", "Async Ruby with Fibers"]
articles = generator.generate_articles(titles)
```

### Tech Stack
- Ruby 3.2+
- Rails 7.1
- HTTParty (HTTP client)
- LLM APIs (OpenAI, Gemini, Perplexity)

---

## 3. 🐍 **LinkedIn Scraper** (Python + Selenium)
**Purpose**: Scrape LinkedIn profiles and export to CSV

### Key Features
- ✅ Selenium-based web scraping
- ✅ Anti-detection measures (headless Chrome, randomized delays)
- ✅ Cookie-based persistence
- ✅ CSV export
- ✅ Multiple scraper variants (basic, enhanced, cookie-based, demo)

### Files
```
linkedin_scraper/
├── main.py                    # Enhanced scraper with anti-detection
├── main_cookies.py            # Cookie-based version
├── demo_scraper.py            # Wikipedia demo (no auth needed)
├── config.json                # Credentials (⚠️ keep secure)
├── profiles_seed.csv          # URLs to scrape
├── requirements.txt           # Dependencies
└── linkedin_profiles.csv      # Output file
```

### Tech Stack
- Python 3.13
- Selenium 4.38
- Pandas
- python-dotenv

---

## 🔄 Integration: Autodialer + AI Blog Generator

The autodialer Rails app **mounts** the AI Blog Generator engine:

```ruby
# autodialer/config/routes.rb
mount AiBlogGenerator::Engine, at: "/blog"
```

This means:
- Main app: `http://localhost:3000` → Autodialer UI
- Blog section: `http://localhost:3000/blog` → AI Blog Generator

**Possible workflow:**
1. User visits `/blog` to read AI-generated articles
2. User returns to `/` to set up call campaigns
3. Articles could inform outbound call scripts

---

## 📊 Comparison Table

| Aspect | Autodialer | AI Blog Generator | LinkedIn Scraper |
|--------|-----------|-------------------|------------------|
| Language | Ruby | Ruby | Python |
| Framework | Rails | Rails Engine | Selenium |
| Purpose | Phone calls | Content generation | Data extraction |
| External API | Twilio | LLMs (OpenAI/Gemini/Perplexity) | LinkedIn |
| Complexity | Medium | Medium | High (anti-detection) |
| Data Flow | Numbers → Calls → Logs | Topics → Articles → DB | Profiles → CSV |

---

## 🎯 Suggested Next Steps

### A: Set Up & Run Autodialer
```bash
cd autodialer
bundle install
# Create .env with Twilio credentials
rails db:create db:migrate
rails server
# Visit http://localhost:3000
```

###  B: Generate Blog Articles
```bash
cd ai_blog_generator
bundle install
# Create .env with LLM API key
rails db:migrate
# Use in Rails console or integrate into autodialer
```

###  C: Improve LinkedIn Scraper
- Use cookie persistence (`main_cookies.py`)
- Add proxy rotation for enhanced anti-detection
- Implement manual login verification workflow




