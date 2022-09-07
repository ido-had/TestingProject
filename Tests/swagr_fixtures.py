import pytest
import requests
from Api.AccountApi import AccountApi
import logging
from Models.Accounts import ApiUserDto,LoginDto,AuthResponseDto

@pytest.fixture(scope="session")
def SwgrUrl(request):
    return request.config.getoption("--urlSwgr")

login=LoginDto("try@gmail.com","testPass")
user=ApiUserDto(login._email,login._password,"testName","testLastNm")
accApi=AccountApi
@pytest.fixture(scope="session")
def registerNewUser(SwgrUrl):
    accApi.postRegister(user)

@pytest.fixture(scope="session")
def loginNewUser(registerNewUser):
    res=accApi.postLogin(login)
    if type(res)==AuthResponseDto:
        pass
    else:
        logging.warning("Error while loading new user data.testing problems may occur")





@pytest.fixture(scope="session")
def AccountApi(SwgrUrl):
    return AccountApi(SwgrUrl)



