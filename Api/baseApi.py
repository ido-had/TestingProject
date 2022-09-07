import json
import requests

class baseApi():
    def __init__(self,url,header:str=None):
        self._url=url
        headers={"accept": "application/json"}
        self._session = requests.session()
        self.session.headers.update(headers)
        if  header:
            self.session.headers.update(headers)





