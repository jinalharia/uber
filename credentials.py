from uber_rides.session import Session
from uber_rides.client import UberRidesClient

session = Session(server_token="AT8uiEHjg8hx785Dnfo2uR48aD3A7B6G13-5N3rf")
client = UberRidesClient(session)

response = client.get_products(51.45, -0.219)
products = response.json.get("products")

# print(products)

response2 = client.get_user_profile()
profile = response2.json

print(profile)