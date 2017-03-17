from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from utils.geolocation import Address
import config.config as config
import pprint
import pandas as pd

class UberRequests():
    def __init__(self, start_address, end_address, number_of_people=None):
        session = Session(server_token=config.server_token)
        client = UberRidesClient(session)
        self.start_address = Address(start_address)
        self.end_address = Address(end_address)

        price_response = client.get_price_estimates(self.start_address.lat, self.start_address.lng, self.end_address.lat, self.end_address.lng,
                                               seat_count=number_of_people)
        estimate = price_response.json.get("prices")
        estimate_df = pd.DataFrame(estimate)
        estimate_df["duration_mins"] = estimate_df["duration"] / 60.0

        pickup_response = client.get_pickup_time_estimates(self.start_address.lat, self.start_address.lng)
        times = pickup_response.json.get("times")
        times_df = pd.DataFrame(times)
        times_df["time_to_pick_up_mins"] = times_df["estimate"] / 60.0
        times_df = times_df.rename(columns={"estimate": "time_to_pick_up"})

        output = pd.merge(estimate_df, times_df, how="outer", on="display_name")
        cols = ["display_name", "time_to_pick_up_mins", "distance", "duration_mins", "currency_code", "estimate",
                "surge_multiplier"]
        self.results = output[cols]
        # pprint.pprint(results)
