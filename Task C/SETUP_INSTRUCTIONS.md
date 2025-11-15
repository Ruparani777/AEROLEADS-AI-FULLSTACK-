# Quick Setup Instructions

## 1. Install Ruby and Rails Dependencies

```bash
# Install bundler if not already installed
gem install bundler

# Install all gems
bundle install
```

## 2. Set Up Database

```bash
# Create database
rails db:create

# Run migrations
rails db:migrate
```

## 3. Configure OpenAI API Key

### Option A: Environment Variable (Windows PowerShell)
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
```

### Option B: Environment Variable (Linux/Mac)
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### Option C: Create .env file (Recommended)
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your-api-key-here
```

**Get your API key from:** https://platform.openai.com/api-keys

## 4. Start the Server

```bash
rails server
```

## 5. Access the Application

Open your browser and visit: **http://localhost:3000**

## 6. Generate Articles

1. Click "New Articles" in the navigation
2. Paste article titles (one per line) in the textarea
3. Click "Generate Articles"
4. Wait for generation to complete
5. View and edit articles as needed

## Sample Titles

You can use the titles from `sample_titles.txt` for testing.

## Troubleshooting

- **API Key Error**: Make sure OPENAI_API_KEY is set correctly
- **Database Error**: Run `rails db:reset` to reset the database
- **Port Already in Use**: Use `rails server -p 3001` to use a different port

