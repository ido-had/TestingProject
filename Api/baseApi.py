import json
import requests

class baseApi():
    def __init__(self,url):
        self._url=url
        header={"accept": "application/json"}
        self._session = requests.session()
        self.session.headers.update(header)




