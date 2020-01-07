from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

class automate:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome()

	def closeBrowser(self):
		self.driver.close()


	def w(self):
		driver = self.driver
		driver.get("https://nucleus.niituniversity.in/")
		driver.maximize_window()
		time.sleep(2)

		user_name_elem = driver.find_element_by_name('SchSel$txtUserName')
		user_name_elem.clear()
		user_name_elem.send_keys(self.username)
		passworword_elem = driver.find_element_by_name('SchSel$txtPassword')
		passworword_elem.clear()
		passworword_elem.send_keys(self.password)
		passworword_elem.send_keys(Keys.RETURN)

		# Select login button
		login_btn = driver.find_element_by_name('SchSel$btnLogin')
		login_btn.click()

		# Select daily dairy button!!		
		daily_diary_btn = driver.find_element_by_name('ctl00$ContentPlaceHolder1$btnDDiary')
		daily_diary_btn.click()
		time.sleep(2)
		in_time = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$Timeinhr'))
		in_time.select_by_value('10')
		out_time = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$Timeouthr'))
		out_time.select_by_value('18')

		work_done = driver.find_element_by_name('ctl00$ContentPlaceHolder1$txtDesc')
		work_done.clear()
		work_done.send_keys('For 1st month i completed Andrew Ng Course and next worked on the project!!!')
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


if __name__ == "__main__":

	username = "U101116FCS142"
	password = "pardhu1998"

	ig = automate(username, password)
	ig.login()
