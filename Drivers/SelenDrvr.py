from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from Tests.Config.Ui_fixtures import SELENIUM, PLAYWRIGHT
from selenium.webdriver import ActionChains
from selenium import webdriver
import time

SELENIUM = 0


class SelenDrvr():
    def __init__(self, driver:webdriver):
        self._driver = driver


    def loadPage(self, url):
        self._driver.get(url)

    def getElement(self, locator, element=None, setData: str = None, click: bool = None):
        if element == None:
            caller = self._driver
        else:
            caller = element
        curr_element = caller.find_element(*locator[SELENIUM])
        self.setDataOrClick(curr_element, setData, click)
        return curr_element

    def getAttr(self, element, attrName: str):
        return element.get_attribute(attrName)

    def setDataOrClick(self, element, setData=None, click=None):
        if setData != None:
            self.sendData(element, setData)
        if click != None:
            element.click()

    def getElementS(self, locator, element=None):
        if element == None:
            caller = self._driver
        else:
            caller = element
        return caller.find_elements(*locator[SELENIUM])

    def getCurrentUrl(self):
        return self._driver.current_url
    def executeScript(self, script,ele):
        if "validationMessage" in script:
            return self.getAttr(ele,"validationMessage")
        else:
            return self._driver.execute_script(script,ele)

    def getTitle(self):
        return self._driver.title

    # ="arguments[0].style.border='2px solid red'"
    def wait(self, element=None):
        WebDriverWait(self._driver, 20).until(
            EC.visibility_of_all_elements_located((element[SELENIUM][0], element[SELENIUM][1])))

    def DragDrop(self, base, dest):
        actions = ActionChains(self._driver)
        actions.drag_and_drop(base, dest).perform()

    def iFrame(self, frame, element, switched=False):
        if not switched:
            WebDriverWait(self._driver,30).until(EC.frame_to_be_available_and_switch_to_it(frame))
        #  self._driver.switch_to.frame(frame)
        self.wait(element)
        try:
            getElement = self.getElement(element)
            return getElement
        except:
            pass
        finally:
            pass

    def switchBackFromIframe(self):
        self._driver.switch_to.default_content()

    def sendData(self, element, data):

        element.send_keys(data)

    def getText(self, element):
        return element.text

    def handleAlert(self):
        pass

    def getAlertMessage(self):
        alert = self._driver.switch_to.alert
        message = alert.text
        alert.accept()
        return message
    # def swithchToAlert(self):
    #     alert= self._driver.switch_to.alert
    #     return alert
