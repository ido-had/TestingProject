import pytest
import logging

@pytest.mark.usefixtures("getLoginPg")

@pytest.mark.integration
def test(getLoginPg):
    pass