from utils.geolocation import Address
import unittest


class TestAddress(unittest.TestCase):
    def test_geolocation(self):
        start_address = "Charing Cross Hospital, Fulham Palace Road, London, W6 8RF"

        address = Address(start_address)
        print(address.lat)
        print(address.lng)

        assert address.lat == 51.48655549999999
        assert address.lng == -0.219482