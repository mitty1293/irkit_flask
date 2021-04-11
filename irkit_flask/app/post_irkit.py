import requests
import json
from const import *

class Post_irkit:
    def __init__(self):
        pass

    def req_post(self, signal):
        msg = json.dumps(signal)
        params = {
            #"clientkey":CLIKEY,
            #"deviceid":DEVID,
            "message":msg
        }
        req = requests.post(URL, params=params)
