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

driver.execute_script("window.open('https://google.com','new window')")
wins = driver.window_handles  #To control which tab to select
time.sleep(2)

driver.switch_to.window(wins[0])
print("This is my zero index: "+ driver.title)

driver.switch_to.window(wins[1])
time.sleep(2)

print("This is my first index: " + driver.title)
time.sleep(5)
driver.quit()