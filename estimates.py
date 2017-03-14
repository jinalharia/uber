from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from utils.geolocation import Address
import pprint
import pandas as pd

session = Session(server_token="AT8uiEHjg8hx785Dnfo2uR48aD3A7B6G13-5N3rf")
client = UberRidesClient(session)

start_address = Address("22 Colebrook Close, London, SW15 3HZ")
end_address = Address("14 Digby Mansions, London, W6 9DE")

response = client.get_products(start_address.lat, start_address.lng)
prod = response.json
products = response.json.get("products")

# print(prod)

response2 = client.get_price_estimates(start_address.lat, start_address.lng, end_address.lat, end_address.lng, seat_count=2)
# prod2 = response2.json
estimate = response2.json.get("prices")
# pprint.pprint(estimate)
# print(len(estimate))

uberX_estimate = next((item for item in estimate if item["display_name"] == "uberX"),None)
# pprint.pprint(uberX_estimate)
# print(uberX_estimate.get("display_name"))
# print(uberX_estimate.get("distance"))
# print(uberX_estimate.get("product_id"))
# print(uberX_estimate.get("estimate"))

response3 = client.get_pickup_time_estimates(start_address.lat, start_address.lng)
times = response3.json.get("times")
pprint.pprint(times)