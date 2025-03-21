import os

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_xpath():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    username = driver.find_element(By.XPATH, "//input[@id='login-username']")
    username.send_keys(os.getenv("USERNAME"))
    print("username entered successfully")

    password = driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys(os.getenv("PASSWORD"))
    print("Password entered successfully")

    submit = driver.find_element(By.XPATH, "//input[@id='js-login-btn']")
    submit.click()
    print("Clicked on sign in button")

    driver.quit()
test_xpath()


