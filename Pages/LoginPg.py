from Pages.BasePage import BasePg
from selenium.webdriver.common.by import By

class LoginPage(BasePg):
    def __init__(self,driver,frmwrk:str):
        super(LoginPage, self).__init__(driver,frmwrk)
    locators={"Email_in":[(By.ID,"email"),"[id='email']"],"Pass_in":[(By.ID,"password"),"[id='password'"]}

    def sendLoginData(self,email:str,passw:str):
        email_in=self.getElement(*self.locators.get("Email_in"),None,email)
        # self.sendData(email_in,email)
        pass_in=self.getElement(*self.locators.get("Pass_in"),None,passw)
        # self.sendData(pass_in,passw)
