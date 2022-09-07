from Api.baseApi import baseApi
from Models.Accounts import *
from Models.General import ProblemDetails

class AccountApi(baseApi):
    def __init__(self,url):
        super().__init__(f"{url}api/Account")


    def postRegister(self,User:ApiUserDto,header:str=None):
        userJson=User.to_json()
        res=self._session.post(url=f"{self._url}/register",data=userJson)
        if res.status_code==200:
            return res.status_code
        elif res.status_code==400:
            return ProblemDetails(**res.json())
        else:
            return res.status_code

    def postLogin(self,login:LoginDto,header:str=None):
        login_json=login.to_json()
        res=self._session.post(url=f"{self._url}/login",data=login_json)
        if res.status_code==200:
            return AuthResponseDto(**res.json())
        elif res.status_code==400:
            return ProblemDetails(**res.json())
        else:
            return res.status_code

    def postRefreshToken(self,data:AuthResponseDto,header:str=None):
        dataJson=data.to_json()
        res=self._session.post(url=f"{self._url}/refreshtoken",data=dataJson)
        if res.status_code==200:
            AuthResponseDto(**res.json())
        elif res.status_code == 400:
            return ProblemDetails(**res.json())
        else:
            return res.status_code
