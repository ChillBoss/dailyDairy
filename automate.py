from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome('C:\\Users\\Pardhu CooL\\automate\\chromedriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()
driver.get('https://nucleus.niituniversity.in')

#username and password
username_field = driver.find_element_by_name('SchSel$txtUserName')
username_field.send_keys('U101116FCS142')
password_field = driver.find_element_by_name('SchSel$txtPassword')
password_field.send_keys('pardhu1998')
time.sleep(1)

#logging in 
login_btn = driver.find_element_by_name('SchSel$btnLogin')
login_btn.click()

#select daily diary
daily_diary_btn = driver.find_element_by_name('ctl00$ContentPlaceHolder1$btnDDiary')
daily_diary_btn.click()
time.sleep(2)

#Select in time and out time
in_time = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$Timeinhr'))
in_time.select_by_value('10')
out_time = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$Timeouthr'))
out_time.select_by_value('18')

work_done = driver.find_element_by_name('ctl00$ContentPlaceHolder1$txtDesc')
work_done.clear()
work_done.send_keys('For 1st month i completed Andrew Ng Course and next worked on the project.')

#submits the daily diary
submit_btn = driver.find_element_by_name('ctl00$ContentPlaceHolder1$btnSubmit')
submit_btn.click()
time.sleep(2)

#click the chrome popup to finish the daily diary entry
popup = driver.switch_to.alert
popup.accept()
time.sleep(3)

driver.quit()
print('***********************************************')
print("Hey Pardhu, I have filled the daily diary for you")
print('***********************************************')
time.sleep(2)





