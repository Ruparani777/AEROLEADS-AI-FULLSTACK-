LinkedIn Profile Scraper

Educational web scraping project using Python and Selenium to extract LinkedIn profile data


📋 Table of Contents


Quick Start


Project Description


Security & Ethics Warning


Features


Installation


Configuration


Usage


Output Format


Troubleshooting


Code Structure


Best Practices


Legitimate Alternatives


License



⚡ Quick Start
# 1. Install dependencies
pip install selenium pandas undetected-chromedriver python-dotenv beautifulsoup4 lxml

# 2. Configure credentials
cp .env.example .env   # or copy manually on Windows

# 3. Add LinkedIn profile URLs to profile_urls.txt

# 4. Run the scraper
python linkedin_scraper.py


⚠️ WARNING: Use only with LinkedIn test accounts for educational purposes. Real accounts may be suspended.


📖 Project Description
This project demonstrates educational web scraping techniques including:


Browser automation with Selenium and undetected-chromedriver


Anti-detection measures for automated browsing


Structured data extraction from dynamic web pages


Handling login, navigation, and delays


Exporting scraped data to CSV


Tech Stack: Python 3.8+, Selenium, undetected-chromedriver, BeautifulSoup4, pandas, python-dotenv
Goal: Learn web scraping fundamentals and Selenium automation in a controlled, ethical environment.

⚠️ Security & Ethics Warning


Legal Risks: Automated scraping violates LinkedIn’s ToS. Accounts may be suspended.


No Commercial Use: Educational purposes only.


Ethical Guidelines: Use test accounts, limit scraping, respect privacy.



🎯 Features


Extract Profile Name, Headline, Location


Capture Current Job, Company, Experience, Education


Extract Top Skills


Store Profile URL and Scraping Timestamp


Export all data to CSV



🛠 Installation
1. Clone Repository
git clone https://github.com/your-repo.git
cd your-repo

2. Create Virtual Environment (Recommended)
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt


Optional: Use conda with environment.yml to avoid Windows build issues.


⚙️ Configuration


Copy .env.example → .env


Add test account credentials:


LINKEDIN_EMAIL=your_test_email@example.com
LINKEDIN_PASSWORD=your_test_password
MAX_PROFILES=20
DELAY_BETWEEN_PROFILES=5
PAGE_LOAD_TIMEOUT=10



Add profile URLs in profile_urls.txt.



💻 Usage
python linkedin_scraper.py



Logs into LinkedIn


Visits each profile with delays


Scrapes data and saves to linkedin_profiles.csv



📊 Output Format
ColumnDescriptionprofile_urlLinkedIn profile URLnameFull nameheadlineProfessional headlinelocationGeographic locationcurrent_titleCurrent job titlecompanyCurrent companyexperience_summarySummary of experienceeducationEducation (top entries)skillsComma-separated skillsscraped_atTimestamp of scraping

🐛 Troubleshooting


Credentials not found: Ensure .env exists with valid credentials


Login fails / CAPTCHA: Use a fresh test account, add longer delays


Element not found: Update CSS selectors in config.py


ChromeDriver mismatch: Use undetected-chromedriver or update Chrome



📂 Code Structure
linkedin_scraper/
├── linkedin_scraper.py
├── config.py
├── requirements.txt
├── .env.example
├── .env
├── profile_urls.txt
├── linkedin_profiles.csv
└── README.md


🚦 Best Practices


Test with 2-3 profiles first


Use test accounts only


Respect rate limits and LinkedIn ToS


Monitor browser while running



🔗 Legitimate Alternatives


LinkedIn API


LinkedIn Sales Navigator


Third-party tools: PhantomBuster, Apify (check ToS)


