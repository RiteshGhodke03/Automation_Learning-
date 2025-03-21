from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()

# Open first website in the main window
driver.get("https://www.google.com")
print("Main Window Title:", driver.title)

# Open a new tab
driver.switch_to.new_window('tab')
driver.get("https://www.bing.com")
print("New Tab Title:", driver.title)

# Open a new window
driver.switch_to.new_window('window')
driver.get("https://www.yahoo.com")
print("New Window Title:", driver.title)

#Get all window handles (IDs)
windows = driver.window_handles
print("\nAll window handles:", windows)

# Switch back to the first tab
driver.switch_to.window(windows[0])
print("Switched back to:", driver.title)

# Switch to the new window (last one opened)
driver.switch_to.window(windows[-1])
print("Switched to last window:", driver.title)

# Close the current window
driver.close()
print("Closed the last window!")

# Go back to the original window
driver.switch_to.window(windows[0])
print("Back to main window:", driver.title)

# Finally, quit the browser
driver.quit()
