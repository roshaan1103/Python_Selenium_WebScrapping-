from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#THis wont work as tha XPATH is wrong and that is the error
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

driver.get("https://alnafi.com")
driver.maximize_window()
time.sleep(5)

driver.execute_script("window.open('https://google.com','new window')")
wins = driver.window_handles
time.sleep(2)

driver.switch_to.window(wins[0])
print("\n=================This is my zero index (alnafi)==============\n"+ driver.title)
mylanfi=driver.find_element(By.XPATH,'//*[@id="__nuxt"]/div/div[4]/section[1]/div[3]/div[1]/div[1]/h1')
print(mylanfi.text)
driver.switch_to.window(wins[1])
time.sleep(2)

print("\n=====================This is my first index(google)=====================\n " + driver.title)
mygoogle = driver.find_element(By.XPATH,'//*[@id="SIvCob"]')
print(mygoogle.text)

time.sleep(5)
driver.quit()