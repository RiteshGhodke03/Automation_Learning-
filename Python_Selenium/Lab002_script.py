from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open Chrome browser
driver = webdriver.Chrome()

# Step 2: Navigate to Google
driver.get("https://www.google.com")

# Step 3: Locate the search box using NAME instead of ID
search_box = driver.find_element(By.NAME, "q")

# Step 4: Enter search text
search_box.send_keys("Selenium Python")

# Step 5: Press Enter to search
search_box.send_keys(Keys.RETURN)

# Step 6: Wait for search results
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))

# Step 7: Print the actual page title
print("Page Title:", driver.title)

# Step 8: Close browser
driver.quit()
