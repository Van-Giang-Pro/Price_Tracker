from sneaker import Sneaker
from flask.views import MethodView
from flask import Flask, render_template, request

product_url = "https://saigonsneaker.com/collections/giay-new-balance/"
product_name = 'New Balance CRT 300 Beige'

app = Flask(__name__)

class HomePage(MethodView):
	def get(self):
		return render_template('index.html')

class PriceTrackingData(MethodView):
	def get(self):
		sneaker = Sneaker(product_url = product_url, product_name = product_name)
		value = sneaker.get_price()
		return render_template('price_data.html', value1 = value, value2 = product_name)

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/price_tracking_data', view_func=PriceTrackingData.as_view('price_tracking_data'))
app.run(debug=True)
