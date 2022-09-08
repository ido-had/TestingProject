import pytest
import requests
from Api.AccountApi import AccountApi
from Api.AuthorsApi import AuthorApi
import logging
from Models.Accounts import ApiUserDto,LoginDto,AuthResponseDto

@pytest.fixture(scope="session")
def SwgrUrl(request):
    return request.config.getoption("--urlSwgr")

login=LoginDto("try@gmail.com","testPass")
user=ApiUserDto(login.email, login.password, "testName", "testLastNm")
accApi=AccountApi(SwgrUrl)

@pytest.fixture(scope="session")
def registerNewUser(SwgrUrl):
    accApi.postRegister(user)

@pytest.fixture(scope="session")
def loginNewUser(registerNewUser):
    res=accApi.postLogin(login)
    if type(res)==AuthResponseDto:
        return res
    else:
        logging.warning("Error while loading new user pre testing. problems may arise")
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


