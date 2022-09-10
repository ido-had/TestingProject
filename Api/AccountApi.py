from Api.baseApi import baseApi
from Models.Accounts import *
from Models.General import ProblemDetails

class AccountApi(baseApi):
    def __init__(self,url,bearer=None,rfrshTkn=None,userId=None):
        super().__init__(f"{url}api/Account",bearer,rfrshTkn,userId)

    def getNewToken(self):
        current_user_tokens=AuthResponseDto(self._userId,self._bearer,self._refreshToken)
        new_tokens=self.postRefreshToken(current_user_tokens)
        self._bearer=new_tokens._token
        self._refreshToken=new_tokens._refreshToken
        self._session.headers.clear()
        self.updatedBearer()
        self.updateHeader()



    def postRegister(self,User:ApiUserDto,header:str=None):
        userJson=User.to_json()
        res=self._session.post(url=f"{self._url}/register",data=userJson)
        if res.status_code==200:
            return res.status_code
        else:
            return f"{res.status_code},{res.text}"

    def postLogin(self,login:LoginDto,header:str=None):
        login_json=login.to_json()
        res=self._session.post(url=f"{self._url}/login",data=login_json)
        if res.status_code==200:
            return AuthResponseDto(**res.json())
        elif res.status_code==400:
            return ProblemDetails(**res.json())
        else:
            return f"{res.status_code},{res.text}"

    def postRefreshToken(self,data:AuthResponseDto,header:str=None):
        dataJson=data.to_json()
        res=self._session.post(url=f"{self._url}/refreshtoken",data=dataJson)
        if res.status_code==200:
            AuthResponseDto(**res.json())
        elif res.status_code == 400:
            return ProblemDetails(**res.json())
        else:
            return f"{res.status_code},{res.text}"
