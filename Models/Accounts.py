from Models.BaseModel import baseObj


class LoginDto(baseObj):
    def __init__(self,email:str,password:str):
        self._email = email
        self._password = password

class ApiUserDto(LoginDto):
    def __init__(self,email:str,password:str,firstName:str,lastName:str):
        super.__init__(email,password)
        self._firstName=firstName
        self._lastName=lastName

class AuthResponseDto(baseObj):
    def __init__(self,userId:str,token:str,refreshToken:str):
        self._userId=userId
        self._token=token
        self._refreshToken=refreshToken



