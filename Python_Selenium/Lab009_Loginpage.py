import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By


def loginpage():
    load_dotenv()
    driver = webdriver.Chrome()
# Navigate to the url
    driver.get("https://app.vwo.com/#/login")
# navigated to Email field and enter username
    email = driver.find_element(By.ID,"login-username")
    email.send_keys(os.getenv("USERNAME"))
#Password field
    password = driver.find_element(By.NAME,"password")
    password.send_keys(os.getenv("PASSWORD"))
#submit button
    submit = driver.find_element(By.ID,"js-login-btn")
    submit.click()
    time.sleep(3)

    error = driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error.text)

    assert error.text == os.getenv("Error_Message")
    print("Testcase passed!!")

    time.sleep(5)
    driver.quit()

loginpage()



