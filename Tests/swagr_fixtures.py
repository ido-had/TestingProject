import pytest
import requests
from Api.AccountApi import AccountApi
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
def AccountApi(SwgrUrl):
    return AccountApi(SwgrUrl)



