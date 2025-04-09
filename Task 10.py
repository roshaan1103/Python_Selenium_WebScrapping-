from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import  encoders
from datetime import *
import time as t

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# List creation to enter and present data into:
course=[]
fees=[]

driver.get("https://alnafi.com/courses/course/linkedin-masterclass")
driver.maximize_window()
t.sleep(5)

driver.execute_script("window.open('https://alnafi.com/courses/course/sysops-administrator','new window')")
wins=driver.window_handles
t.sleep(5)

#For 1st tab:
driver.switch_to.window(wins[0])
course_name=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[5]/div/div[2]/div/div[1]/h1").text
fees_pkr=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[5]/div/div[2]/div/div[2]/div/div[2]/div[1]/p[1]").text
course.append(course_name)
fees.append(fees_pkr)

t.sleep(5)

#For 2nd tab:
driver.switch_to.window(wins[1])
course_name=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[5]/div/div[2]/div/div[1]/h1").text
fees_pkr=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[5]/div/div[2]/div/div[2]/div/div[2]/div[1]/p[1]").text
course.append(course_name)
fees.append(fees_pkr)

#Print the list:
print(course)
print(fees)

# CSV File
data=list(zip(course,fees))
print(data)

file=open('Al-Nafi_Course_fee.csv','w',newline="")
write=csv.writer(file)
write.writerows(data)
file.close()

t.sleep(5)
driver.quit()

day=date.today()
time1=datetime.now()

my_custom=day.strftime("%B %d %Y")
current_time=time1.strftime("%I:%M:%S %p")

filename=r"D:\Al-nafi\DevOps\Python Selenium\PythonSeleniumProject\Selenium_Python_Learn\Practical Assigment\Al-Nafi_Course_fee.csv"

msg=MIMEMultipart()

my_mail="roshaan1357@gmail.com"
password="khan1103"

msg['Subject']= f"Alnafi Course fees details :  {my_custom} {current_time}"
msg['From']= my_mail
msg['To'] = my_mail
msg['Cc'] = 'roshaan1103@gmail.com'

#Body section
body="""
<html><p> Hi Team,<br> We have collected Alanfi's course fees details from offical website and we have stored data into CSV file, So kindly find and attach.   <br><br><br>Roshaan<br> <img src="cid:alogo" width="100" height="50"></p> </html>
"""
msg.attach(MIMEText(body,'html'))

#Attachment Section:
attachment=open(filename,'rb')
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename=%s" % filename)
msg.attach(part)


connection=smtplib.SMTP('smtp.gmail.com')
connection.starttls()       #TLS transport layer security


connection.login(user=my_mail,password=password)
connection.send_message(msg)
connection.close()