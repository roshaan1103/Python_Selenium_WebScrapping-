from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

driver.get("https://alnafi.com")
driver.maximize_window()
time.sleep(5)
print(driver.title)

driver.execute_script("window.open('https://google.com','new window')")
print(driver.title)
time.sleep(5)

driver.quit()