from utils.geolocation import Address
import unittest


class TestAddress(unittest.TestCase):
    def test_geolocation(self):
        start_address = "15 Digby Mansions, London, W6 9DE"

        address = Address(start_address)
        print(address.lat)
        print(address.lng)

        assert address.lat == 51.4898825
        assert address.lng == -0.2292357