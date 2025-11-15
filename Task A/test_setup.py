"""
Test script to verify setup before running the main scraper
"""

import sys
import os

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python version: {version.major}.{version.minor}.{version.micro}")
        print("   Required: Python 3.8 or higher")
        return False

def check_dependencies():
    """Check if all required packages are installed"""
    required_packages = [
        'selenium',
        'pandas',
        'undetected_chromedriver',
        'dotenv',
        'bs4',
        'lxml'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'dotenv':
                __import__('dotenv')
            elif package == 'bs4':
                __import__('bs4')
            else:
                __import__(package)
            print(f"✅ {package} installed")
        except ImportError:
            print(f"❌ {package} NOT installed")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️ Missing packages: {', '.join(missing_packages)}")
        print("   Run: pip install -r requirements.txt")
        return False
    
    return True

def check_env_file():
    """Check if .env file exists and has required variables"""
    if not os.path.exists('.env'):
        print("❌ .env file not found")
        print("   Copy .env.example to .env and add your credentials")
        return False
    
    print("✅ .env file exists")
    
    # Check if credentials are set
    from dotenv import load_dotenv
    load_dotenv()
    
    email = os.getenv('LINKEDIN_EMAIL')
    password = os.getenv('LINKEDIN_PASSWORD')
    
    if not email or not password or email == 'your_test_email@example.com':
        print("⚠️ .env file exists but credentials not configured")
        print("   Edit .env and add your LinkedIn test account credentials")
        return False
    
    print("✅ LinkedIn credentials configured")
    return True

def check_profile_urls():
    """Check if profile_urls.txt exists and has URLs"""
    if not os.path.exists('profile_urls.txt'):
        print("❌ profile_urls.txt not found")
        return False
    
    print("✅ profile_urls.txt exists")
    
    with open('profile_urls.txt', 'r') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    if not urls:
        print("⚠️ profile_urls.txt is empty")
        print("   Add LinkedIn profile URLs (one per line)")
        return False
    
    print(f"✅ Found {len(urls)} profile URL(s)")
    return True

def test_chrome_availability():
    """Test if Chrome browser is available"""
    try:
        import undetected_chromedriver as uc
        print("✅ undetected_chromedriver imported successfully")
        
        # Try to create a driver (this will download chromedriver if needed)
        print("🔧 Testing Chrome driver initialization...")
        options = uc.ChromeOptions()
        options.add_argument('--headless')
        
        driver = uc.Chrome(options=options)
        driver.quit()
        
        print("✅ Chrome driver initialized successfully")
        return True
        
    except Exception as e:
        print(f"❌ Chrome driver test failed: {str(e)}")
        print("   Make sure Google Chrome is installed")
        return False

def main():
    """Run all setup checks"""
    print("=" * 70)
    print("🔍 LINKEDIN SCRAPER - SETUP CHECK")
    print("=" * 70)
    print()
    
    all_passed = True
    
    print("1️⃣ Checking Python version...")
    all_passed &= check_python_version()
    print()
    
    print("2️⃣ Checking dependencies...")
    all_passed &= check_dependencies()
    print()
    
    print("3️⃣ Checking environment file...")
    all_passed &= check_env_file()
    print()
    
    print("4️⃣ Checking profile URLs file...")
    all_passed &= check_profile_urls()
    print()
    
    print("5️⃣ Testing Chrome driver...")
    all_passed &= test_chrome_availability()
    print()
    
    print("=" * 70)
    if all_passed:
        print("✅ ALL CHECKS PASSED!")
        print("You're ready to run: python linkedin_scraper.py")
    else:
        print("❌ SOME CHECKS FAILED")
        print("Please fix the issues above before running the scraper")
    print("=" * 70)

if __name__ == "__main__":
    main()
