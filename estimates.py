from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from utils.geolocation import Address
import pprint
import pandas as pd

session = Session(server_token="AT8uiEHjg8hx785Dnfo2uR48aD3A7B6G13-5N3rf")
client = UberRidesClient(session)

start_address = Address("Charing Cross Hospital, Fulham Palace Road, London, W6 8RF")
end_address = Address("14 Digby Mansions, London, W6 9DE")

response = client.get_products(start_address.lat, start_address.lng)
products = response.json.get("products")
products_df = pd.DataFrame(products)
# pprint.pprint(products_df)

response2 = client.get_price_estimates(start_address.lat, start_address.lng, end_address.lat, end_address.lng, seat_count=2)
estimate = response2.json.get("prices")
estimate_df = pd.DataFrame(estimate)
estimate_df["duration_mins"] = estimate_df["duration"] / 60.0
# pprint.pprint(estimate_df)
# print(len(estimate))
# uberX_estimate = next((item for item in estimate if item["display_name"] == "uberX"),None)
# pprint.pprint(uberX_estimate)
# print(uberX_estimate.get("display_name"))
# print(uberX_estimate.get("distance"))
# print(uberX_estimate.get("product_id"))
# print(uberX_estimate.get("estimate"))

response3 = client.get_pickup_time_estimates(start_address.lat, start_address.lng)
times = response3.json.get("times")
times_df = pd.DataFrame(times)
times_df["time_to_pick_up_mins"] = times_df["estimate"] / 60.0
times_df = times_df.rename(columns={"estimate":"time_to_pick_up"})
# times_df.to_clipboard()
# pprint.pprint(times_df)

output = pd.merge(estimate_df, times_df, how="outer", on="display_name")
cols = ["display_name","time_to_pick_up_mins", "distance", "duration_mins", "currency_code", "estimate", "surge_multiplier"]
output_formatted = output[cols]
pprint.pprint(output_formatted)