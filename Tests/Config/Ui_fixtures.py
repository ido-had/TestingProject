import pytest
from playwright.sync_api import sync_playwright
from selenium import webdriver
from Pages.LoginPg import LoginPage
from selenium.webdriver.chrome.options import Options
from Drivers.SelenDrvr import SelenDrvr
from Drivers.PlayrightDrvr import PlayrghtDrvr
import allure
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
def getRemoteDrvr(getCmdExec):
    pass

@pytest.fixture(scope="function")
def web_browser(getFrmwrk,getdriverPath,getBrowser,request,getCmdExec):
    if getFrmwrk==PLAYWRIGHT:
        p = sync_playwright().start()
        if getBrowser=="C":
            browser = p.chromium.launch(args=['--start-maximized'], headless=False)
        elif getBrowser=="F":
            browser=p.firefox.launch(args=['--start-maximized'], headless=False)
        browser=browser.new_page(no_viewport=True)
    else:
        if getdriverPath!="remote":
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            browser = webdriver.Chrome(executable_path=getdriverPath,chrome_options=chrome_options)
            browser.maximize_window()
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.set_capability("browserVersion", "105.0")
            chrome_options.set_capability("platformName", "LINUX")
            #{"browserName":"chrome","browserVersion":"105.0","platformName":"LINUX","se:noVncPort":7900,"se:vncEnabled":true}
            chrome_options.set_capability("browserName","chrome")
            chrome_options.set_capability("se:noVncPort",7900)
            chrome_options.set_capability("se:vncEnabled",True)
            browser = webdriver.Remote(
                command_executor=getCmdExec,
                options=chrome_options)
    b=browser

    # Return browser instance to test case:
    yield b

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            b.screenshot(full_page=True, type="png")
            allure.attach(b.screenshot(full_page=True, type="png"),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            b.execute_script("document.body.bgColor = 'white';")

            allure.attach(b.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)


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


# @pytest.fixture(scope="function")
# def web_browser(request,browser,getFrmwrk):
#
#    b=browser
#
#    # Return browser instance to test case:
#    yield b
#
#    # Do teardown (this code will be executed after each test):
#
#    if request.node.rep_call.failed:
#        # Make the screen-shot if test failed:
#        try:
#            b.screenshot(full_page=True, type="png")
#            allure.attach(b.screenshot(full_page=True, type="png"),
#                          name=request.function.__name__,
#                          attachment_type=allure.attachment_type.PNG)
#        except:
#            b.execute_script("document.body.bgColor = 'white';")
#
#            allure.attach(b.get_screenshot_as_png(),
#                          name=request.function.__name__,
#                          attachment_type=allure.attachment_type.PNG)
#
#
#    # Close browser window:
#    b.close()


# @pytest.fixture(scope="function")
# def web_browser(request,getChromePath):
#     # Open browser:
#     b = webdriver.Chrome(executable_path=getChromePath)
#     b.maximize_window()
#     # Return browser instance to test case:
#     yield b
#
#     # Do teardown (this code will be executed after each test):
#
#     if request.node.rep_call.failed:
#         # Make the screen-shot if test failed:
#         try:
#             b.execute_script("document.body.bgColor = 'white';")
#
#             allure.attach(b.get_screenshot_as_png(),
#                           name=request.function.__name__,
#                           attachment_type=allure.attachment_type.PNG)
#         except:
#             pass # just ignore
#
#     # Close browser window:
#     b.quit()

