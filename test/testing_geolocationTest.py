from utils.geolocation import Address
import unittest


class TestAddress(unittest.TestCase):
    def test_geolocation(self):
        start_address = "22 Colebrook Close, London, SW15 3HZ"
        end_address = "15 Digby Mansions, London, W6 9DE"

        colebrook_address = Address(start_address)
        # print(colebrook_address.lat)
        # print(colebrook_address.lng)

        assert colebrook_address.lat == 51.4505949
        assert colebrook_address.lng == -0.2197215