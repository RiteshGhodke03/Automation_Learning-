from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service(r"C:\Users\Ritesh Ghodke\Downloads\chrome-win64 (1)\chrome-win64\chrome.exe")

driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Print page title
print("Page Title:", driver.title)

# Close browser
driver.quit()
