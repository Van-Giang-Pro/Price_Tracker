import requests
from bs4 import BeautifulSoup


class Sneaker:

	def __init__(self, product_url, product_name):
		self.product_url = product_url
		self.product_name = product_name

	def get_price(self):
		name_price_dict = dict()
		r = requests.get(self.product_url)
		soup = BeautifulSoup(r.content, "html.parser")
		for object_html in soup.findAll('li'):
			for name in object_html.findAll('h2', class_='woocommerce-loop-product__title'):
				name = name.text
			for price in object_html.findAll('span', class_='woocommerce-Price-amount amount'):
				price = price.text
				name_price_dict[name] = price
				print(f"{name} - {price}")
		return name_price_dict[self.product_name]


if __name__ == "__main__":
	product_url = "https://saigonsneaker.com/collections/giay-new-balance/"
	product_name = 'New Balance CRT 300 Beige'
	sneaker = Sneaker(product_url, product_name)
	sneaker.get_price()