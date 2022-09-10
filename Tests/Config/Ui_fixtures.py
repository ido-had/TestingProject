import pytest



SELENIUM = 0
PLAYWRIGHT = 1

@pytest.hookimpl( hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)
@pytest.fixture(scope="function")
def browser(getFrmwrk,getdriverPath):
    if getFrmwrk==PLAYWRIGHT:
        p = sync_playwright().start()
        browser = p.chromium.launch(args=['--start-maximized'], headless=False)
        return browser.new_page(no_viewport=True)
    else:
        b = webdriver.Chrome(executable_path=getdriverPath)
        b.maximize_window()
        return b

@pytest.fixture(scope="function")
def web_browser(request,browser,getFrmwrk):
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