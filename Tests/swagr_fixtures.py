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
        logging.warning("Error while loading new user pre testing. problems may occur")
@pytest.fixture(scope="session")
def getBearer(loginNewUser):
    my_token=loginNewUser._token
    headers = {'Authorization': f'Bearer {my_token}'}
    return headers
@pytest.fixture(scope="session")
def getAccountApi(SwgrUrl):
    return AccountApi(SwgrUrl)

@pytest.fixture(scope="session")
def getAuthorApi(SwgrUrl,getBearer):
    return AuthorApi(SwgrUrl,getBearer)


