"""
LinkedIn Profile Scraper
WARNING: This tool is for EDUCATIONAL PURPOSES ONLY.
- LinkedIn's Terms of Service prohibit automated scraping
- Use ONLY with test accounts you own
- Never scrape production LinkedIn without explicit permission
- This may violate LinkedIn's ToS and could result in account suspension
"""

import time
import random
import csv
from datetime import datetime
from typing import List, Dict, Optional
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import config


class LinkedInScraper:
    """LinkedIn profile scraper using Selenium with anti-detection measures"""
    
    def __init__(self):
        self.driver = None
        self.profiles_data = []
        
    def setup_driver(self):
        """Initialize undetected Chrome driver with anti-detection settings"""
        print("🔧 Setting up Chrome driver...")
        
        # Create options outside try block to ensure it's available in exception handler
        options = uc.ChromeOptions()
        
        # Anti-detection measures
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument(f'user-agent={random.choice(config.USER_AGENTS)}')
        
        if config.HEADLESS_MODE:
            options.add_argument('--headless')
        
        try:
            # Initialize driver - let it auto-detect Chrome version
            # Try with version_main=141 to match current Chrome version
            try:
                self.driver = uc.Chrome(options=options, use_subprocess=False, version_main=141)
            except:
                # If that fails, try auto-detection
                self.driver = uc.Chrome(options=options, use_subprocess=False)
            
            # Wait a moment for the browser to fully initialize
            time.sleep(1)
            
            self.driver.implicitly_wait(config.IMPLICIT_WAIT)
            
            # Try to maximize window, but don't fail if it doesn't work
            try:
                self.driver.maximize_window()
            except Exception as max_error:
                print(f"⚠️ Could not maximize window: {str(max_error)}")
                # Try to set window size instead
                try:
                    self.driver.set_window_size(1920, 1080)
                except:
                    pass  # Ignore if this also fails
            
            print("✅ Driver setup complete")
        except Exception as e:
            error_msg = str(e)
            print(f"❌ Error setting up driver: {error_msg}")
            
            # Check if it's a version mismatch error
            if "ChromeDriver only supports Chrome version" in error_msg or "version" in error_msg.lower():
                print("💡 ChromeDriver version mismatch detected!")
                print("   Attempting to download correct ChromeDriver version...")
                try:
                    # Create fresh options object for retry
                    retry_options = uc.ChromeOptions()
                    retry_options.add_argument('--disable-blink-features=AutomationControlled')
                    retry_options.add_argument('--disable-dev-shm-usage')
                    retry_options.add_argument('--no-sandbox')
                    retry_options.add_argument(f'user-agent={random.choice(config.USER_AGENTS)}')
                    
                    if config.HEADLESS_MODE:
                        retry_options.add_argument('--headless')
                    
                    # Force download of correct ChromeDriver version
                    self.driver = uc.Chrome(options=retry_options, use_subprocess=False, version_main=141)
                    self.driver.implicitly_wait(config.IMPLICIT_WAIT)
                    self.driver.maximize_window()
                    print("✅ Driver setup complete (after downloading correct version)")
                except Exception as e2:
                    print(f"❌ Failed to setup driver after retry: {str(e2)}")
                    print("\n💡 Solutions:")
                    print("   1. Update Google Chrome to the latest version (recommended)")
                    print("   2. Or manually delete ChromeDriver cache and let it re-download")
                    print("   3. Run: pip install --upgrade undetected-chromedriver")
                    raise
            else:
                # For other errors, just raise
                raise
        
    def login(self):
        """Login to LinkedIn using credentials from config"""
        print("🔐 Logging into LinkedIn...")
        
        if not config.LINKEDIN_EMAIL or not config.LINKEDIN_PASSWORD:
            raise ValueError("LinkedIn credentials not found in .env file!")
        
        try:
            self.driver.get('https://www.linkedin.com/login')
            time.sleep(random.uniform(2, 4))
            
            # Enter email
            email_field = self.driver.find_element(By.ID, 'username')
            email_field.send_keys(config.LINKEDIN_EMAIL)
            time.sleep(random.uniform(0.5, 1.5))
            
            # Enter password
            password_field = self.driver.find_element(By.ID, 'password')
            password_field.send_keys(config.LINKEDIN_PASSWORD)
            time.sleep(random.uniform(0.5, 1.5))
            
            # Click login button
            login_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            login_button.click()
            
            # Wait for login to complete
            time.sleep(random.uniform(4, 6))
            
            # Check if login was successful
            if 'feed' in self.driver.current_url or 'mynetwork' in self.driver.current_url:
                print("✅ Login successful")
                return True
            else:
                print("⚠️ Login may have failed - please check manually")
                print(f"Current URL: {self.driver.current_url}")
                input("Press Enter after manually resolving any issues...")
                return True
                
        except Exception as e:
            print(f"❌ Login error: {str(e)}")
            raise
    
    def human_like_scroll(self):
        """Simulate human-like scrolling behavior"""
        # Scroll down slowly
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        current_position = 0
        scroll_increment = random.randint(300, 500)
        
        while current_position < total_height:
            current_position += scroll_increment
            self.driver.execute_script(f"window.scrollTo(0, {current_position});")
            time.sleep(random.uniform(0.3, 0.7))
            
            # Update total height (page might load more content)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height > total_height:
                total_height = new_height
    
    def safe_find_element(self, by: By, selector: str, timeout: int = 5) -> Optional[str]:
        """Safely find element and return its text, return None if not found"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, selector))
            )
            return element.text.strip()
        except (TimeoutException, NoSuchElementException):
            return None
    
    def safe_find_elements(self, by: By, selector: str, timeout: int = 5) -> List:
        """Safely find multiple elements, return empty list if not found"""
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((by, selector))
            )
            return elements
        except (TimeoutException, NoSuchElementException):
            return []
    
    def scrape_profile(self, profile_url: str) -> Dict:
        """Scrape a single LinkedIn profile"""
        print(f"\n📊 Scraping: {profile_url}")
        
        profile_data = {
            'profile_url': profile_url,
            'name': None,
            'headline': None,
            'location': None,
            'current_title': None,
            'company': None,
            'experience_summary': None,
            'education': None,
            'skills': None,
            'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        try:
            # Check if driver session is still valid
            try:
                _ = self.driver.current_url
            except Exception:
                print("❌ Browser session lost. Reinitializing...")
                self.setup_driver()
                self.login()
            
            # Navigate to profile
            self.driver.get(profile_url)
            time.sleep(random.uniform(3, 5))
            
            # Scroll to load all content
            self.human_like_scroll()
            time.sleep(random.uniform(2, 3))
            
            # Get page source for parsing
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            
            # Extract name
            name_elem = self.safe_find_element(By.CSS_SELECTOR, 'h1.text-heading-xlarge')
            if name_elem:
                profile_data['name'] = name_elem
            
            # Extract headline
            headline_elem = self.safe_find_element(By.CSS_SELECTOR, 'div.text-body-medium.break-words')
            if headline_elem:
                profile_data['headline'] = headline_elem
            
            # Extract location
            location_elem = self.safe_find_element(By.CSS_SELECTOR, 'span.text-body-small.inline.t-black--light.break-words')
            if location_elem:
                profile_data['location'] = location_elem
            
            # Extract current experience (first experience entry)
            try:
                experience_section = self.driver.find_element(By.CSS_SELECTOR, '#experience')
                # Find the first experience item
                exp_items = self.driver.find_elements(By.CSS_SELECTOR, 'li.artdeco-list__item')
                if exp_items:
                    first_exp = exp_items[0]
                    title_elem = first_exp.find_elements(By.CSS_SELECTOR, 'span[aria-hidden="true"]')
                    if len(title_elem) >= 1:
                        profile_data['current_title'] = title_elem[0].text.strip()
                    if len(title_elem) >= 2:
                        profile_data['company'] = title_elem[1].text.strip()
                
                # Get experience summary
                all_exp_text = experience_section.text
                profile_data['experience_summary'] = all_exp_text[:500] if len(all_exp_text) > 500 else all_exp_text
                
            except NoSuchElementException:
                print("⚠️ Experience section not found")
            
            # Extract education
            try:
                edu_section = self.driver.find_element(By.CSS_SELECTOR, '#education')
                edu_items = edu_section.find_elements(By.CSS_SELECTOR, 'li.artdeco-list__item')
                education_list = []
                for edu in edu_items[:3]:  # Get top 3 education entries
                    edu_text = edu.text.strip()
                    if edu_text:
                        education_list.append(edu_text.replace('\n', ' | '))
                profile_data['education'] = '; '.join(education_list)
                
            except NoSuchElementException:
                print("⚠️ Education section not found")
            
            # Extract skills
            try:
                # Click "Show all skills" if available
                show_all_buttons = self.driver.find_elements(By.XPATH, 
                    "//a[contains(@class, 'artdeco-button') and contains(., 'Show all')]")
                
                for button in show_all_buttons:
                    if 'skill' in button.text.lower():
                        button.click()
                        time.sleep(random.uniform(1, 2))
                        break
                
                # Extract skills
                skills_section = self.driver.find_element(By.CSS_SELECTOR, '#skills')
                skill_items = skills_section.find_elements(By.CSS_SELECTOR, 'span[aria-hidden="true"]')
                skills_list = []
                for skill in skill_items[:10]:  # Get top 10 skills
                    skill_text = skill.text.strip()
                    if skill_text and len(skill_text) > 2:
                        skills_list.append(skill_text)
                
                # Remove duplicates and join
                profile_data['skills'] = ', '.join(list(dict.fromkeys(skills_list[:10])))
                
            except NoSuchElementException:
                print("⚠️ Skills section not found")
            
            print(f"✅ Successfully scraped: {profile_data['name']}")
            
        except Exception as e:
            print(f"❌ Error scraping profile: {str(e)}")
        
        return profile_data
    
    def scrape_multiple_profiles(self, profile_urls: List[str]):
        """Scrape multiple LinkedIn profiles with delays"""
        total = len(profile_urls)
        print(f"\n🎯 Starting scraping of {total} profiles...")
        print(f"⏱️ Estimated time: {total * config.DELAY_BETWEEN_PROFILES / 60:.1f} minutes")
        
        for index, url in enumerate(profile_urls, 1):
            print(f"\n[{index}/{total}] Processing profile...")
            
            profile_data = self.scrape_profile(url)
            self.profiles_data.append(profile_data)
            
            # Add delay between profiles (except for the last one)
            if index < total:
                delay = random.uniform(config.DELAY_BETWEEN_PROFILES, config.DELAY_BETWEEN_PROFILES + 3)
                print(f"⏳ Waiting {delay:.1f} seconds before next profile...")
                time.sleep(delay)
        
        print(f"\n✅ Scraping complete! Processed {len(self.profiles_data)} profiles")
    
    def save_to_csv(self):
        """Save scraped data to CSV file"""
        if not self.profiles_data:
            print("⚠️ No data to save")
            return
        
        df = pd.DataFrame(self.profiles_data)
        df.to_csv(config.OUTPUT_CSV, index=False, encoding='utf-8-sig')
        print(f"💾 Data saved to {config.OUTPUT_CSV}")
        print(f"📊 Total profiles saved: {len(self.profiles_data)}")
    
    def close(self):
        """Close the browser"""
        if self.driver:
            try:
                self.driver.quit()
                print("🔒 Browser closed")
            except Exception as e:
                # Ignore cleanup errors as they're not critical
                print(f"⚠️ Warning during browser cleanup: {str(e)}")
                try:
                    self.driver = None
                except:
                    pass


def load_profile_urls(file_path: str) -> List[str]:
    """Load profile URLs from text file"""
    urls = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and 'linkedin.com' in line:
                    urls.append(line)
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return []
    
    return urls


def main():
    """Main execution function"""
    print("=" * 70)
    print("🚨 LINKEDIN PROFILE SCRAPER - EDUCATIONAL USE ONLY 🚨")
    print("=" * 70)
    print("\n⚠️ WARNING:")
    print("- This tool is for LEARNING purposes only")
    print("- Use ONLY with test accounts you own")
    print("- LinkedIn ToS prohibits automated scraping")
    print("- Your account may be suspended if detected")
    print("- Do NOT use for commercial purposes")
    print("\n" + "=" * 70 + "\n")
    
    # Confirmation prompt
    confirmation = input("Do you understand the risks and agree to use this responsibly? (yes/no): ")
    if confirmation.lower() != 'yes':
        print("❌ Exiting - User did not confirm")
        return
    
    # Load profile URLs
    profile_urls = load_profile_urls(config.PROFILE_URLS_FILE)
    
    if not profile_urls:
        print(f"❌ No valid profile URLs found in {config.PROFILE_URLS_FILE}")
        print("Please add LinkedIn profile URLs to the file (one per line)")
        return
    
    # Limit to MAX_PROFILES
    if len(profile_urls) > config.MAX_PROFILES:
        print(f"⚠️ Found {len(profile_urls)} URLs, limiting to {config.MAX_PROFILES}")
        profile_urls = profile_urls[:config.MAX_PROFILES]
    
    print(f"📋 Loaded {len(profile_urls)} profile URLs")
    
    # Initialize scraper
    scraper = LinkedInScraper()
    
    try:
        # Setup and login
        scraper.setup_driver()
        scraper.login()
        
        # Scrape profiles
        scraper.scrape_multiple_profiles(profile_urls)
        
        # Save results
        scraper.save_to_csv()
        
    except KeyboardInterrupt:
        print("\n⚠️ Interrupted by user")
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        import traceback
        print("\n📋 Full error traceback:")
        traceback.print_exc()
    finally:
        try:
            scraper.close()
        except Exception as e:
            print(f"⚠️ Error during cleanup: {str(e)}")
        print("\n✅ Program finished")


if __name__ == "__main__":
    main()
