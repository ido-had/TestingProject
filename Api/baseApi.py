import json
import requests


class baseApi():
    def __init__(self, url, bearer: str = None, refreshToken: str = 0, userId: int = None):
        self._url = url
        self._userId = userId
        self._refreshToken = refreshToken
        self._session = requests.session()
        self._bearer = bearer
        self.updateHeader()
        if bearer:
            self.updatedBearer(bearer)

    def updatedBearer(self, bearer):
        self._bearer = bearer
        headers = {'Authorization': f'Bearer {bearer}'}
        self._session.headers.update(headers)

    def updateHeader(self):
        headers = {"accept": "application/json","Content-Type": "application/json"}
        self._session.headers.update(headers)

