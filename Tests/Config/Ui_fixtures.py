import pytest
from playwright.sync_api import sync_playwright
from selenium import webdriver
from Pages.LoginPg import LoginPage
from selenium.webdriver.chrome.options import Options
from Drivers.SelenDrvr import SelenDrvr
from Drivers.PlayrightDrvr import PlayrghtDrvr
import allure
import json

SELENIUM = 0
PLAYWRIGHT = 1

@pytest.mark.usefixtures("get_url")
@pytest.mark.usefixtures("getdriverPath")
@pytest.mark.usefixtures("getBrowser")
@pytest.mark.usefixtures("getCmdExec")

@pytest.fixture(scope="session")
def getFrmwrk(request):
    if request.config.getoption("--frmwrk") == "P":
        return PLAYWRIGHT
    else:
        return SELENIUM


@pytest.fixture(scope="session")
def getCapPath(request):
    filePath=request.config.getoption("--CapPath")

    return filePath

@pytest.fixture(scope="session")
def Playrightbrowser(getBrowser,getFrmwrk):
    if getFrmwrk == PLAYWRIGHT:
        p = sync_playwright().start()
        if getBrowser == "C":
            browser = p.chromium.launch(args=['--start-maximized'], headless=False)
        elif getBrowser == "F":
            browser = p.firefox.launch(args=['--start-maximized'], headless=False)
        return browser
    else:
        return None

@pytest.fixture(scope="function")
def web_browser(getFrmwrk,getdriverPath,Playrightbrowser,request,getCmdExec,getCapPath):
    if getFrmwrk==PLAYWRIGHT:
        browser=Playrightbrowser.new_page(no_viewport=True)
    else:
        if getdriverPath!="remote":
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            browser = webdriver.Chrome(executable_path=getdriverPath,chrome_options=chrome_options)
            browser.maximize_window()
        else:
            Capabilties = open(getCapPath, "r")
            #{"browserName":"chrome","browserVersion":"105.0","platformName":"LINUX","se:noVncPort":7900,"se:vncEnabled":true}
            browser = webdriver.Remote(
                command_executor=getCmdExec,
                desired_capabilities=json.load(Capabilties))
    b=browser

    # Return browser instance to test case:
    yield b

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        if getFrmwrk==PLAYWRIGHT:
            try:
                b.screenshot(full_page=True, type="png")
                allure.attach(b.screenshot(full_page=True, type="png"),
                              name=request.function.__name__,
                              attachment_type=allure.attachment_type.PNG)
            except:
                pass
        else:
            try:
                allure.attach(b.get_screenshot_as_png(),
                              name=request.function.__name__,
                              attachment_type=allure.attachment_type.PNG)
            except:
                pass
    # Close browser window:
    b.close()


@pytest.fixture(scope="function")
def getDriver(getFrmwrk,web_browser):
    if getFrmwrk==SELENIUM:
        return SelenDrvr(web_browser)
    else:
        return PlayrghtDrvr(web_browser)


@pytest.fixture(scope="function")
def getLoginPg(getDriver,get_url):
    logPg=LoginPage(getDriver)
    logPg._driver.loadPage(get_url)
    return logPg

@pytest.fixture(scope="function")
def getUnloadedPg(getDriver):
    return LoginPage(getDriver)

