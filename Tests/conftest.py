from playwright.sync_api import sync_playwright
from selenium import webdriver
import allure
from Tests.Config.swagr_fixtures import *
from Tests.Config.Ui_fixtures import *

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="localhost/")
    parser.addoption("--urlSwgr", action="store", default="http://localhost:7017/")
    parser.addoption("--drvrPath",action="store",default="C:\\as")
    parser.addoption("--frmwrk",action="store",default="S")
    parser.addoption("--browser",action="store",default="chrome")

@pytest.fixture(scope="session")
def get_url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="session")
def getdriverPath(request):
    return request.config.getoption("--drvrPath")

@pytest.fixture(scope="session")
def getFrmwrk(request):
    if request.config.getoption("--frmwrk") == "P":
        return PLAYWRIGHT
    else:
        return SELENIUM

@pytest.fixture(scope="session")
def getBrowser(request):
    return request.config.getoption("--browser")