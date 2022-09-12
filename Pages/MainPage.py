from Pages.BasePage import BasePg
from selenium.webdriver.common.by import By

class MainPage(BasePg):
    def __init__(self,driver,frmwrk:str):
        super().__init__(driver,frmwrk)

    locators={}

