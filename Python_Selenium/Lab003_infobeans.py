from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests

# Define URLs for Staging and Live
STAGING_URL = "https://staging.infobeans.com/"
LIVE_URL = "https://www.infobeans.com/"

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# Path to your ChromeDriver (update the path as needed)
service = Service(r"C:\Users\Ritesh Ghodke\Downloads\chrome-win64 (2)\chrome-win64\chrome.exe")  # Replace with full path if needed
driver = webdriver.Chrome(service=service, options=chrome_options)


def get_page_details(url):
    """Fetches page title, meta description, and H1 headers."""
    driver.get(url)
    time.sleep(3)  # Wait for page to load

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    title = soup.title.string if soup.title else "No title"
    meta_desc = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta_desc["content"] if meta_desc else "No meta description"

    h1_tags = [h1.get_text(strip=True) for h1 in soup.find_all("h1")]

    return {"title": title, "meta_desc": meta_desc, "h1_tags": h1_tags}


def check_broken_links(url):
    """Checks for broken links (404 errors) on a page."""
    driver.get(url)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    links = [a.get("href") for a in soup.find_all("a", href=True)]

    broken_links = []
    for link in links:
        if link.startswith("http"):  # Only check absolute URLs
            try:
                response = requests.head(link, allow_redirects=True, timeout=5)
                if response.status_code == 404:
                    broken_links.append(link)
            except requests.RequestException:
                broken_links.append(link)

    return broken_links


# Fetch details for staging and live versions
staging_data = get_page_details(STAGING_URL)
live_data = get_page_details(LIVE_URL)

# Check broken links
staging_broken_links = check_broken_links(STAGING_URL)
live_broken_links = check_broken_links(LIVE_URL)

# Capture screenshots
driver.get(STAGING_URL)
driver.save_screenshot("staging_screenshot.png")

driver.get(LIVE_URL)
driver.save_screenshot("live_screenshot.png")

# Close the browser
driver.quit()

# Display results
print("\n🔹 Title Comparison:")
print(f"Staging: {staging_data['title']}")
print(f"Live: {live_data['title']}")

print("\n🔹 Meta Description Comparison:")
print(f"Staging: {staging_data['meta_desc']}")
print(f"Live: {live_data['meta_desc']}")

print("\n🔹 H1 Headers Comparison:")
print(f"Staging: {staging_data['h1_tags']}")
print(f"Live: {live_data['h1_tags']}")

print("\n🔹 Broken Links:")
print(f"Staging Broken Links: {staging_broken_links}")
print(f"Live Broken Links: {live_broken_links}")

print("\n✅ Screenshots saved: 'staging_screenshot.png' and 'live_screenshot.png'")
