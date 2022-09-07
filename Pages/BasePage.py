from playwright.sync_api import Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.conftest import SELENIUM, PLAYWRIGHT
from selenium.webdriver import ActionChains

class BasePg():
    def __init__(self, driver, frmwork):
        self._driver = driver
        self.frameWork = frmwork

    _locators = {"Backbtn": [(By.CLASS_NAME, "back"), "has text:BACK"]}

    def getElement(self, locator,element=None):
        if not element:
            element=self._driver
        if self.frameWork == SELENIUM:
            return element.find_element(locator[SELENIUM])
        else:
            try:
                elements = element.locator(locator[PLAYWRIGHT])
            except:
                elements = element.query_selector(locator[PLAYWRIGHT])
            finally:
                return elements
    def getElementS(self,locator,element=None):
        if not element:
            element=self._driver
        if self.frameWork:
            return element.query_selector_all(locator[PLAYWRIGHT])
        else:
            return self.getElement(locator,element)

    def paintElement(self, element):
        if self.frameWork == PLAYWRIGHT:
            element.evaluate("arguments[0].style.border='2px solid red'")
        else:
            self._driver.execute_script("arguments[0].style.border='2px solid red'", element)

    def wait(self,element=None):
        if self.frameWork:
            self._driver.wait_for_load_state()
        else:
            WebDriverWait(self._driver, 20).until(EC.visibility_of_element_located(element))

    def DragDrop(self,base,dest):
        if self.frameWork:
            base.hover()
            self._driver.mouse.down()
            box=dest.boundingBox()
            self._driver.mouse.move(box.x + box.width / 2, box.y + box.height / 2)
            dest.hover()
            self._driver.mouse.up()
        else:
            actions = ActionChains(self._driver)
            actions.drag_and_drop(base,dest).perform()
    def iFrame(self,frame):
        if self.frameWork:
            pass
        else:
            self._driver.switch_to.frame(frame)



if __name__ == '__main__':
    locators = {"Backbtn": [(By.CLASS_NAME, "back"), "has text:BACK"]}
    print(*locators.get("Backbtn")[0])
