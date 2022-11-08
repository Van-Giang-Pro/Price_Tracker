"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome = Service('C:/Users/Admin/PycharmProjects/Price_Tracker/chromedriver.exe')
driver = webdriver.Chrome(service=chrome)


class Product:
	def __init__(self, name, price_drop_notification):
		self.name = name
		self.price_drop_notification = price_drop_notification

	def tracker_price(self):
		driver.get('https://www.google.com')

	def __del__(self):
		print('The object is destroyed.')pip install -U selenium


product = Product("nike jordan", 300000)
product.tracker_price()
print(type(driver))
"""

########################################################################################################

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome = Service('C:/Users/Admin/PycharmProjects/Price_Tracker/chromedriver.exe')
driver = webdriver.Chrome(service=chrome)
driver.get('https://techwithtim.net')
print(driver.title)
print("\n")
search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
	main = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "main"))
	)
	articles = main.find_elements(By.TAG_NAME, "article")
	for article in articles:
		header = article.find_element(By.CLASS_NAME, "entry-summary")
		print(header.text)
		print("\n")
finally:
	driver.quit()
"""

########################################################################################################

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome = Service('C:/Users/Admin/PycharmProjects/Price_Tracker/chromedriver.exe')
driver = webdriver.Chrome(service=chrome)
driver.get('https://techwithtim.net')
link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

try:
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
	)
	element.click()

	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "sow-button-19310003"))
	)
	element.click()

	driver.back()
	driver.back()
	driver.back()
	driver.forward()
	driver.forward()
except:
	driver.quit()
"""

########################################################################################################

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

chrome = Service('C:/Users/Admin/PycharmProjects/Price_Tracker/chromedriver.exe')
driver = webdriver.Chrome(service=chrome)
driver.get('https://orteil.dashnet.org/cookieclicker/')
driver.implicitly_wait(10)

langbutton = driver.find_element(By.ID, "langSelect-EN")
langbutton.click()

driver.implicitly_wait(20)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, ("productPrice" + str(i))) for i in range(1, -1, -1)]

for i in range(5000):
	actions = ActionChains(driver)
	actions.click(cookie)
	actions.perform()
	count = int(cookie_count.text.split(" ")[0])
	for item in items:
		value = int(item.text)
		if value <= count:
			upgrade_actions = ActionChains(driver)
			upgrade_actions.move_to_element(item)
			upgrade_actions.click()
			upgrade_actions.perform()

driver.quit()

