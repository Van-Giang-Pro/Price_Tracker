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
		print('The object is destroyed.')


product = Product("nike jordan", 300000)
product.tracker_price()
print(type(driver))
