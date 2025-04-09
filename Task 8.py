from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# List creation to enter and present data into:
course=[]
fees=[]

driver.get("https://alnafi.com/courses/course/linkedin-masterclass")
driver.maximize_window()
time.sleep(5)

driver.execute_script("window.open('https://alnafi.com/courses/course/sysops-administrator','new window')")
wins=driver.window_handles
time.sleep(5)

#For 1st tab:
driver.switch_to.window(wins[0])
course_name=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[5]/div/div[2]/div/div[1]/h1").text
fees_pkr=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[5]/div/div[2]/div/div[2]/div/div[2]/div[1]/p[1]").text
course.append(course_name)
fees.append(fees_pkr)

time.sleep(5)

#For 2nd tab:
driver.switch_to.window(wins[1])
course_name=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[5]/div/div[2]/div/div[1]/h1").text
fees_pkr=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[5]/div/div[2]/div/div[2]/div/div[2]/div[1]/p[1]").text
course.append(course_name)
fees.append(fees_pkr)

#Print the list:
print(course)
print(fees)

time.sleep(5)
driver.quit()