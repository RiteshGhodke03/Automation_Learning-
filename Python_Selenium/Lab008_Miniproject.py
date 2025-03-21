#### Automation the mini project
#1. Navigate to the URL
#2. Find the button
#3. Click on it
#4. Verify that URL changes or new URL comes.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def miniproject():
    driver = webdriver.Edge()
    print("Navigating to the URL...")
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    print("Finding the 'Make Appointment' button...")
    make_element= driver.find_element(By.ID, "btn-make-appointment")

    print("Clicking the 'Make Appointment' button...")
    make_element.click()

    print("Verifying the URL...")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    print("Test Passed: URL has changed successfully.")

    time.sleep(5)
    driver.quit()

miniproject()