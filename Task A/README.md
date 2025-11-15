# LinkedIn Profile Scraper

> **Educational web scraping project using Python and Selenium to extract LinkedIn profile data**

## 📋 Table of Contents
- [Quick Start](#-quick-start)
- [Project Description](#-project-description)
- [Security & Ethics Warning](#️-security--ethics-warning)
- [How to Run Locally](#-how-to-run-locally)
- [Features](#-features)
- [Configuration](#️-configuration)
- [Troubleshooting](#-troubleshooting)
- [Live Demo](#-live-demo)

---

## ⚡ Quick Start

```bash
# 1. Install dependencies
pip install selenium pandas undetected-chromedriver python-dotenv beautifulsoup4 lxml

# 2. Configure credentials (edit .env file)
copy .env.example .env

# 3. Add profile URLs to profile_urls.txt

# 4. Run the scraper
python linkedin_scraper.py
```

**⚠️ WARNING:** This violates LinkedIn's ToS. Use ONLY with test accounts for educational purposes. Your account WILL be suspended if detected.

---

## 📖 Project Description

This is an **educational web scraping project** that demonstrates how to:
- Automate browser interactions using **Selenium** and **undetected-chromedriver**
- Implement anti-detection techniques to avoid bot detection
- Extract structured data from dynamic web pages
- Handle authentication and navigation flows
- Export scraped data to CSV format

**What it does:** Automatically logs into LinkedIn, navigates to specified profile URLs, extracts key information (name, headline, experience, education, skills), and saves the data to a CSV file.

**Technology Stack:**
- **Python 3.8+** - Core programming language
- **Selenium 4.x** - Browser automation framework
- **undetected-chromedriver** - Stealth Chrome driver to bypass detection
- **BeautifulSoup4** - HTML parsing and data extraction
- **Pandas** - CSV data handling and export
- **python-dotenv** - Secure credential management

**Use Case:** Learning web scraping fundamentals, understanding anti-bot measures, and practicing Python automation skills in a controlled educational environment.

---

## ⚠️ SECURITY & ETHICS WARNING

**READ THIS BEFORE USING THIS TOOL**

### Legal Warnings

1. **LinkedIn Terms of Service**: LinkedIn's Terms of Service **EXPLICITLY PROHIBIT** automated scraping and data collection. Using this tool may violate these terms.

2. **Account Suspension Risk**: LinkedIn actively detects and blocks automated bots. Your account **WILL LIKELY BE SUSPENDED** if detected.

3. **Legal Risks**: Depending on your jurisdiction, automated scraping may violate:
   - Computer Fraud and Abuse Act (CFAA) in the US
   - GDPR in Europe
   - Similar data protection laws worldwide

4. **No Commercial Use**: This tool is provided for **EDUCATIONAL PURPOSES ONLY**. Do not use it for commercial purposes.

### Ethical Guidelines

- ✅ **DO**: Use with test accounts you own
- ✅ **DO**: Limit scraping to small samples (~20 profiles)
- ✅ **DO**: Respect people's privacy
- ❌ **DON'T**: Scrape production LinkedIn
- ❌ **DON'T**: Scrape without explicit permission
- ❌ **DON'T**: Use scraped data for spam or harassment
- ❌ **DON'T**: Sell or redistribute scraped data

### Our Stance

This project is a **learning exercise** to understand web scraping, Selenium automation, and anti-detection techniques. The authors:
- Do not encourage violating LinkedIn's ToS
- Are not responsible for any consequences of misuse
- Recommend using LinkedIn's official API for legitimate use cases

**By using this tool, you accept ALL risks and responsibilities.**

---

## 🎯 Features

This scraper extracts the following information from LinkedIn profiles:

- **Profile Name**
- **Headline** (current role description)
- **Location**
- **Current Job Title**
- **Current Company**
- **Experience Summary** (last 500 characters)
- **Education** (top 3 entries)
- **Top Skills** (up to 10 skills)
- **Profile URL**
- **Timestamp** of scraping

---

## 🚀 How to Run Locally

### Prerequisites

Before running this scraper, ensure you have:

1. ✅ **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
2. ✅ **Google Chrome browser** - [Download Chrome](https://www.google.com/chrome/)
3. ✅ **LinkedIn test account** - Create a NEW test account (never use your real account!)
4. ✅ **Git** (optional) - For cloning the repository
5. ✅ **Basic command line knowledge**

### Installation & Setup

### Step 1: Clone or Download This Repository

```bash
cd
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Optional: Recommended (Conda) setup for Windows

If pip attempted to compile packages like `pandas` (build errors on Windows), use the provided `environment.yml` which installs pre-built binary packages via `conda` (conda-forge). This avoids lengthy MSVC builds.

```powershell
# create the conda environment (requires conda/miniconda/Anaconda installed)
conda env create -f environment.yml

# activate it
conda activate aeroleads-task-a

# then run the scraper (same commands as below)
python linkedin_scraper.py
```

Notes:
- `environment.yml` pins Python 3.11 and installs `pandas` and `lxml` as conda packages (binary wheels).
- Other packages from `requirements.txt` are installed via pip inside the environment to preserve compatibility.
- If you prefer `pip` and your Python already has compatible binary wheels, the `pip install -r requirements.txt` approach still works.

### Step 4: Configure Environment Variables ⚙️

**IMPORTANT:** Never commit your `.env` file to version control!

1. Copy `.env.example` to `.env`:
   ```bash
   # Windows
   copy .env.example .env
   
   # macOS/Linux
   cp .env.example .env
   ```

2. Edit `.env` and add your **TEST ACCOUNT** credentials:
   ```env
   # LinkedIn Test Account Credentials (NEVER use your real account!)
   LINKEDIN_EMAIL=your_test_email@example.com
   LINKEDIN_PASSWORD=your_test_password
   
   # Scraping Configuration
   MAX_PROFILES=20                    # Maximum number of profiles to scrape
   DELAY_BETWEEN_PROFILES=5           # Seconds to wait between profiles (anti-detection)
   PAGE_LOAD_TIMEOUT=10               # Page load timeout in seconds
   ```

**Environment Variables Explained:**

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `LINKEDIN_EMAIL` | LinkedIn test account email | - | ✅ Yes |
| `LINKEDIN_PASSWORD` | LinkedIn test account password | - | ✅ Yes |
| `MAX_PROFILES` | Max profiles to scrape per run | 20 | ❌ No |
| `DELAY_BETWEEN_PROFILES` | Delay between profiles (seconds) | 5 | ❌ No |
| `PAGE_LOAD_TIMEOUT` | Page load timeout (seconds) | 10 | ❌ No |

**Security Best Practices:**
- ✅ Use a dedicated test account created specifically for this project
- ✅ Never use your real LinkedIn credentials
- ✅ Never commit `.env` file to Git (it's in `.gitignore`)
- ✅ Use strong, unique passwords even for test accounts
- ❌ Don't share your `.env` file with anyone

### Step 5: Add Profile URLs

Edit `profile_urls.txt` and add LinkedIn profile URLs (one per line):

```
https://www.linkedin.com/in/username1/
https://www.linkedin.com/in/username2/
https://www.linkedin.com/in/username3/
```

**Note**: Only add profiles you have permission to access!

## 📖 Usage

### Basic Usage

```bash
python linkedin_scraper.py
```

The script will:
1. Display legal warnings and ask for confirmation
2. Load profile URLs from `profile_urls.txt`
3. Launch Chrome browser and login to LinkedIn
4. Scrape each profile with human-like delays
5. Save data to `linkedin_profiles.csv`

### Expected Output

```
🚨 LINKEDIN PROFILE SCRAPER - EDUCATIONAL USE ONLY 🚨
⚠️ WARNING: [legal warnings displayed]

Do you understand the risks and agree to use this responsibly? (yes/no): yes

📋 Loaded 5 profile URLs
🔧 Setting up Chrome driver...
✅ Driver setup complete
🔐 Logging into LinkedIn...
✅ Login successful

🎯 Starting scraping of 5 profiles...
⏱️ Estimated time: 0.4 minutes

[1/5] Processing profile...
📊 Scraping: https://www.linkedin.com/in/example1/
✅ Successfully scraped: John Doe
⏳ Waiting 5.2 seconds before next profile...

[2/5] Processing profile...
...

✅ Scraping complete! Processed 5 profiles
💾 Data saved to linkedin_profiles.csv
📊 Total profiles saved: 5
🔒 Browser closed
```

## 📊 Output Format

The scraper generates a CSV file (`linkedin_profiles.csv`) with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `profile_url` | LinkedIn profile URL | https://linkedin.com/in/johndoe |
| `name` | Full name | John Doe |
| `headline` | Professional headline | Senior Software Engineer at Tech Co |
| `location` | Geographic location | San Francisco, CA |
| `current_title` | Current job title | Senior Software Engineer |
| `company` | Current company | Tech Company Inc. |
| `experience_summary` | Summary of experience section | Senior Software Engineer... |
| `education` | Educational background | Stanford University \| Computer Science |
| `skills` | Comma-separated skills | Python, Java, Machine Learning... |
| `scraped_at` | Timestamp of scraping | 2024-11-06 14:30:45 |

## ⚙️ Configuration

Edit `config.py` or `.env` to customize:

### Environment Variables

- `LINKEDIN_EMAIL`: Your test account email
- `LINKEDIN_PASSWORD`: Your test account password
- `MAX_PROFILES`: Maximum profiles to scrape (default: 20)
- `DELAY_BETWEEN_PROFILES`: Delay in seconds between profiles (default: 5)
- `PAGE_LOAD_TIMEOUT`: Page load timeout in seconds (default: 10)

### Advanced Settings (config.py)

- `HEADLESS_MODE`: Run browser in background (default: False)
- `IMPLICIT_WAIT`: Selenium implicit wait time (default: 10)
- `USER_AGENTS`: List of user agents for rotation

## 🛡️ Anti-Detection Features

This scraper implements several anti-detection measures:

1. **undetected-chromedriver**: Patches Chrome to avoid detection
2. **Realistic User Agents**: Rotates between realistic user agent strings
3. **Human-like Delays**: Random delays between actions (3-6 seconds)
4. **Smooth Scrolling**: Simulates human scrolling behavior
5. **Random Wait Times**: Varies timing to avoid patterns
6. **Proper Browser Flags**: Disables automation flags

### Additional Recommendations

For even better stealth (not implemented):
- Use residential proxies
- Rotate IP addresses
- Implement CAPTCHA solving
- Use authenticated sessions
- Add cookie management

## 🐛 Troubleshooting

### Issue: "LinkedIn credentials not found"
**Solution**: Make sure you've created a `.env` file with your credentials.

### Issue: Login fails or redirects to CAPTCHA
**Solution**: 
- LinkedIn may have detected automation
- Try logging in manually first
- Use a fresh test account
- Add longer delays

### Issue: Elements not found / Scraping fails
**Solution**:
- LinkedIn frequently changes their HTML structure
- Update CSS selectors in `config.py` → `SELECTORS`
- Use browser DevTools to find new selectors

### Issue: ChromeDriver version mismatch
**Solution**: 
- `undetected-chromedriver` auto-downloads the correct version
- If issues persist, manually update Chrome browser

### Issue: Account suspended
**Solution**:
- This is expected if LinkedIn detects automation
- Create a new test account
- Use only for educational purposes

## 📝 Code Structure

```
aeroleads task A/
│
├── linkedin_scraper.py    # Main scraper script
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Your credentials (DO NOT commit!)
├── profile_urls.txt      # Input: List of profile URLs
├── linkedin_profiles.csv # Output: Scraped data
└── README.md            # This file
```

## 🔧 How It Works

1. **Setup**: Initializes undetected Chrome driver with anti-detection flags
2. **Login**: Automates LinkedIn login using provided credentials
3. **Navigation**: Navigates to each profile URL with human-like delays
4. **Scrolling**: Scrolls through the page to load dynamic content
5. **Extraction**: Uses CSS selectors to extract profile data
6. **Parsing**: Cleans and formats the extracted data
7. **Storage**: Saves data to CSV using pandas
8. **Cleanup**: Closes browser and releases resources

## 🚦 Best Practices

1. **Start Small**: Test with 2-3 profiles first
2. **Use Test Accounts**: Never use your real LinkedIn account
3. **Monitor Activity**: Watch the browser to ensure it's working
4. **Respect Rate Limits**: Don't scrape hundreds of profiles
5. **Check LinkedIn ToS**: Always respect their terms
6. **Consider Alternatives**: Use LinkedIn API for legitimate purposes

## 🔗 Legitimate Alternatives

Instead of scraping, consider these legal options:

- **LinkedIn API**: Official API for authorized access
- **LinkedIn Sales Navigator**: Paid tool for prospecting
- **RapidAPI LinkedIn**: Third-party APIs with proper authorization
- **Manual Export**: Use LinkedIn's built-in export features

## 📜 License

This project is provided "as-is" for **EDUCATIONAL PURPOSES ONLY**.

**The authors are not responsible for:**
- Any misuse of this tool
- Account suspensions or bans
- Legal consequences
- Data protection violations
- Any other damages or liabilities

## 🤝 Contributing

This is an educational project. If you find bugs or improvements:
- Update selectors if LinkedIn changes their HTML
- Improve anti-detection measures
- Add better error handling
- Enhance documentation

## 📞 Support

For educational questions:
- Review the code and comments
- Check troubleshooting section
- Understand Selenium and web scraping basics

**Remember**: This is a learning tool. Use responsibly!

---

## 🌐 Live Demo

**⚠️ IMPORTANT:** This project cannot be hosted as a live demo for the following reasons:

### Why No Live Demo?

1. **Legal & Ethical Concerns**
   - LinkedIn's Terms of Service explicitly prohibit automated scraping
   - Hosting a live scraper would violate ToS and could result in legal action
   - We do not want to encourage or facilitate ToS violations at scale

2. **Security Risks**
   - Requires LinkedIn credentials which should never be shared or stored on public servers
   - Credentials could be intercepted or stolen if hosted publicly
   - Would create security vulnerabilities for users

3. **Technical Limitations**
   - Requires Chrome browser and ChromeDriver on the server
   - LinkedIn actively blocks cloud/datacenter IP addresses
   - Would require significant infrastructure (proxies, CAPTCHA solving)

4. **Ethical Responsibility**
   - This is an **educational project** for learning purposes only
   - Intended to be run locally on personal machines with test accounts
   - Not designed for production use or mass scraping

### Alternative Demonstrations

If you want to see this project in action:

- ✅ **Run it locally** following the [How to Run Locally](#-how-to-run-locally) instructions
- ✅ **Watch the browser automation** in real-time on your machine
- ✅ **Review the code** to understand how it works
- ✅ **Test with 2-3 profiles** to see the CSV output
- ✅ **Record a video** of your local run for portfolio purposes (blur credentials!)

### Legitimate Alternatives for Production

If you need LinkedIn data for legitimate purposes:

| Service | Description | Use Case |
|---------|-------------|----------|
| [LinkedIn API](https://developer.linkedin.com/) | Official LinkedIn API | Authorized integrations |
| [LinkedIn Sales Navigator](https://business.linkedin.com/sales-solutions/sales-navigator) | Paid prospecting tool | B2B sales & recruiting |
| [PhantomBuster](https://phantombuster.com/) | Cloud automation platform | Marketing automation (check ToS) |
| [Apify](https://apify.com/) | Web scraping platform | Data extraction (check ToS) |

**Remember:** Always respect LinkedIn's Terms of Service and obtain proper authorization before collecting data.

---

## 📊 Sample Output

Here's what the CSV output looks like (with anonymized data):

| profile_url | name | headline | location | current_title | company | skills |
|-------------|------|----------|----------|---------------|---------|--------|
| linkedin.com/in/user1 | John Doe | Software Engineer at Tech Co | San Francisco, CA | Senior Engineer | Tech Company | Python, JavaScript, AWS, Docker |
| linkedin.com/in/user2 | Jane Smith | Product Manager | New York, NY | PM | Startup Inc | Product Strategy, Agile, SQL |

**File Location:** `linkedin_profiles.csv` (created in project root after running)

---


