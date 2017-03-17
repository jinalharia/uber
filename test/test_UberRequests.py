from utils.uber import UberRequests
import config.config as config
import pprint

req = UberRequests(config.hospital, config.digby)
pprint.pprint(req.results)
