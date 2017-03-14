import json, urllib, urllib.parse
from urllib.request import urlopen

address = "22 Colebrook Close, London, SW15 3HZ"
end_address = "15 Digby Mansions, London, W6 9DE"

class Address():

    def __init__(self, address):
        encodedAddress = urllib.parse.quote_plus(address)
        data = urlopen(
            "http://maps.googleapis.com/maps/api/geocode/json?address=" + encodedAddress + '&sensor=false').read()
        location = json.loads(data)['results'][0]['geometry']['location']
        self.lat = location['lat']
        self.lng = location['lng']
