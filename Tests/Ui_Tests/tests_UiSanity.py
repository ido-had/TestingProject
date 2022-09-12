import pytest
import Pages

@pytest.mark.usefixtures("getLoginPg")

def test1(getLoginPg):
    getLoginPg.sendLoginData("tttt","1234")

