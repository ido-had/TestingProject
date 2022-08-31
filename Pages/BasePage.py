from playwright.sync_api import Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from Tests.conftest import SELENIUM,PLAYWRIGHT



class BasePg():
    def __init__(self, driver, frmwork):
        self._driver = driver
        self.frameWork = frmwork

    _locators={"Backbtn":[(By.CLASS_NAME,"back"),"has text:BACK"]}

    def getElement(self,locator):
        if self.frameWork==SELENIUM:
            return self._driver.find_element(locator[SELENIUM])
        else:
            try:
                element= self._driver.locator(locator[PLAYWRIGHT])
            except:
                element= self._driver.query_selector(locator[PLAYWRIGHT])
            finally:
                return element

    def paintElement(self,element):
        if self.frameWork==PLAYWRIGHT:
            element.evaluate("arguments[0].style.border='2px solid red'")
        else:
            self._driver.execute_script("arguments[0].style.border='2px solid red'",element)


if __name__ == '__main__':
    locators = {"Backbtn": [(By.CLASS_NAME, "back"), "has text:BACK"]}
    print(*locators.get("Backbtn")[0])
