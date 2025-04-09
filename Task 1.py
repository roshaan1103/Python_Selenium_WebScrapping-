from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://m.cricbuzz.com/cricket-stats/icc-rankings/men/batting')
driver.maximize_window()

#rows
rows=driver.find_elements(By.XPATH,"/html/body/div/main/div[2]/div[1]/div/div/div[2]/div") #it was div[2] at the end...remove [2] so that it takes every rows
rows_count= len(rows)
rows_count= rows_count-1 # -1 as we have to ignore the headers div it counted

#columns:
columns=driver.find_elements(By.XPATH,"/html/body/div/main/div[2]/div[1]/div/div/div[2]/div[1]/div")
columns_count=len(columns)

#Total:

print("Total numbers of rows:",rows_count, "and Total number of columns:",columns_count)

time.sleep(2)
driver.quit()