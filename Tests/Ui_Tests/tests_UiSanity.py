import pytest
import Pages

@pytest.mark.usefixtures("getLoginPg")

def test1(getLoginPg):
    getLoginPg.sendLoginData("tttt@sdf.xo","1234")
    getLoginPg.RegisterOrBackToLogin()
    getLoginPg.sendRegisterData("asdas","ssss")


