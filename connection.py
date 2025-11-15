from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, OrderType
from py_clob_client.order_builder.constants import BUY
import requests as req

price_url = "https://clob.polymarket.com/price"
price_res = req.url(price_url)
# returns JSON { "price" : 1234.0}

