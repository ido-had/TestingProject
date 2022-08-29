from playwright.sync_api import Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from Tests.conftest import SELENIUM,PLAYWRIGHT



class BasePg():
    def __init__(self, driver, frmwork):
        self._driver = driver
        self.frameWork = frmwork

    locators={"Backbtn":[(By.CLASS_NAME,"back"),"has text:BACK"]}

    def getElement(self,locator):
        if self.frameWork==SELENIUM:
            pass
        else:
            pass



if __name__ == '__main__':
    locators = {"Backbtn": [(By.CLASS_NAME, "back"), "has text:BACK"]}
    print(*locators.get("Backbtn")[1])
