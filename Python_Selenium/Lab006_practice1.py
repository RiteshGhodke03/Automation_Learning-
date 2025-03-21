
from selenium import webdriver


def test():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service" in driver.page_source:
        print("Text Found !! test case passed")
    else:
        print("Text not found in page source")

