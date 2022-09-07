from Api.baseApi import baseApi
from Models.Accounts import *

class AccountApi(baseApi):
    def __init__(self,url):
        super.__init__(url)


    def postRegister(self,User,header=None):
        pass
    def postLogin(self,login,header=None):
        pass
    def postRefreshToken(self,header=None):
        pass