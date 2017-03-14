import json, urllib, urllib.parse
from urllib.request import urlopen

class Address():

    def __init__(self, address):
        encodedAddress = urllib.parse.quote_plus(address)
        data = urlopen(
            "http://maps.googleapis.com/maps/api/geocode/json?address=" + encodedAddress + '&sensor=false').read()
        location = json.loads(data)['results'][0]['geometry']['location']
        self.lat = location['lat']
        self.lng = location['lng']
