import pytest
from playwright.sync_api import sync_playwright
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure

SELENIUM=0
PLAYWRIGHT=1

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://automationpractice.com/index.php")
    parser.addoption("--drvrPath",action="store",default="C:\\Users\ohad\\Documents\\sela\\chromedriver_win32\\chromedriver.exe")
    parser.addoption("--frmwrk",action="store",default="s")

@pytest.fixture(scope="session")
def get_url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="session")
def getdriverPath(request):
    return request.config.getoption("--drvrPath")

@pytest.fixture(scope="session")
def getFrmwrk(request):
    if request.config.getoption("--frmwrk") =="p":
        return PLAYWRIGHT
    else:
        return SELENIUM


