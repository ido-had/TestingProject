import pytest
import requests
from Api.AccountApi import AccountApi
from Api.AuthorsApi import AuthorApi
from Api.BooksApi import BooksApi
import logging
from Models.Accounts import ApiUserDto,LoginDto,AuthResponseDto



login=LoginDto("try@gmail.com","testPass")
user=ApiUserDto(login.email, login.password, "testName", "testLastNm")

@pytest.mark.usefixtures("SwgrUrl")
@pytest.fixture(scope="session")
def registerNewUser(SwgrUrl):
    accApi = AccountApi(SwgrUrl)
    accApi.postRegister(user)
    return accApi

@pytest.fixture(scope="session")
def loginNewUser(registerNewUser):
    res=registerNewUser.postLogin(login)
    if type(res)==AuthResponseDto:
        return res
    else:
        logging.warning("Error while loading user data. problems may arise")
# @pytest.fixture(scope="session")
# def getBearer(loginNewUser):
#     my_token=loginNewUser._token
#     return my_token
# @pytest.fixture(scope="session")
# def getrfrshTkn(loginNewUser):
#     rfrshTkn=loginNewUser._refreshToken
#     return rfrshTkn
@pytest.fixture(scope="session")
def getAccountApi(SwgrUrl,loginNewUser):
    return AccountApi(SwgrUrl,loginNewUser._token,loginNewUser._refreshToken,loginNewUser._userId)

@pytest.fixture(scope="session")
def getAuthorApi(SwgrUrl,loginNewUser):
    return AuthorApi(SwgrUrl,loginNewUser._token,loginNewUser._refreshToken,loginNewUser._userId)
@pytest.fixture(scope="session")
def getBooksApi(SwgrUrl,loginNewUser):
    return BooksApi(SwgrUrl,loginNewUser._token,loginNewUser._refreshToken,loginNewUser._userId)

