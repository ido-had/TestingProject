from Pages.BasePage import BasePg
from selenium.webdriver.common.by import By

class AuthorPg(BasePg):
    def __init__(self,driver,frmWork):
        super(AuthorPg, self).__init__(driver,frmWork)

    locators={}