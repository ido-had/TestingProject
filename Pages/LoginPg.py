from Pages.BasePage import BasePg
from selenium.webdriver.common.by import By

class LoginPage(BasePg):
    def __init__(self,driver,frmwrk:str):
        super(LoginPage, self).__init__(driver,frmwrk)
    locators={"Email_in":[(By.ID,"email"),"[id='email']"],"Pass_in":[(By.ID,"password"),"[id='password'"],"Submit":[(By.CLASS_NAME,"btn-primary"),"[type='submit']"],
              "Register":[(By.CLASS_NAME,"btn"),"[type='button']"]}

    def sendLoginData(self,email:str,passw:str):
        email_element=self.getElement(self.locators.get("Email_in"),None,email)
        self.getElement(self.locators.get("Pass_in"),None,passw)
        self.getElement(self.locators.get("Submit"), None, None, "click")
        return self.getAttr(email_element,"validationMessage")

    def submit(self):
        self.getElement(self.locators.get("Submit"), None, None, "click")


