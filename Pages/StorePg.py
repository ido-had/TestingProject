from Pages.BasePage import BasePg
from selenium.webdriver.common.by import By

class StorePage(BasePg):
    def __init__(self,driver):
        super(StorePage, self).__init__(driver)

    locators={}


