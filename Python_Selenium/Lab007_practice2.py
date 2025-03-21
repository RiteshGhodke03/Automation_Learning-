from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://app.vwo.com/")
print(driver.title)
if "Sign in to VWO platform" in driver.page_source:
    print("Test case passed")
else:
    print("Testcase Failed")