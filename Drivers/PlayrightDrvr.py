from playwright.sync_api import Page
from selenium import webdriver

PLAYWRIGHT=1
class PlayrghtDrvr():
    def __init__(self,driver:Page):
        self._driver=driver

    def loadPage(self, url):
        self._driver.goto(url)

    def getElement(self, locator, element=None, setData: str = None, click: bool = None):
        if element == None:
            caller = self._driver
        else:
            caller = element
        try:
            curr_element = caller.locator(locator[PLAYWRIGHT])
        except:
            curr_element = caller.query_selector(locator[PLAYWRIGHT])
        finally:
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
        return caller.query_selector_all(locator[PLAYWRIGHT])

    def paintElement(self, element):
        element.evaluate("arguments[0].style.border='2px solid red'")

    def wait(self, element=None):
        self._driver.wait_for_load_state()

    def DragDrop(self, base, dest):
        base.hover()
        self._driver.mouse.down()
        box = dest.boundingBox()
        self._driver.mouse.move(box.x + box.width / 2, box.y + box.height / 2)
        dest.hover()
        self._driver.mouse.up()

    def iFrame(self, frame, element, switched=False):
        return self._driver.frameLocator('iframe').locator(element[PLAYWRIGHT])

    def sendData(self, element, data):
        element.type(data)

    def getText(self, element):
        return element.text_content()

    def switchBackFromIframe(self):
        pass


    def handleAlert(self):
        self._driver.on("dialog", handle)

    def getAlertMessage(self):
        return message

def handle(dialog):
    global message
    message=dialog.message
    dialog.accept()

