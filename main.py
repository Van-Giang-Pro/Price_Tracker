from selenium import webdriver
from selenium.webdriver.chrome.service import Service


global driver
class Product:
	def __init__(self, name, price_drop_notification):
		self.name = name
		self.price_drop_notification = price_drop_notification

	def tracker_price(self):
		chrome = Service('C:/Users/fs120806/Desktop/Document/Python OOP/Price_Tracker/chromedriver.exe')
		driver = webdriver.Chrome(service=chrome)
		driver.get('https://www.google.com')


product = Product("nike jordan", 300000)
product.tracker_price()
