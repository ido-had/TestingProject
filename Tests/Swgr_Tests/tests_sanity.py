import pytest


@pytest.mark.usefixtures("getAccountApi")


def test1(getAccountApi):
    assert True
