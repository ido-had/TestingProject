from Pages.BasePage import BasePg
from selenium.webdriver.common.by import By

class LoginPage(BasePg):
    def __init__(self,driver,frmwrk:str):
        super(LoginPage, self).__init__(driver,frmwrk)
    locators={"Email_in":[(By.ID,"email"),"[id='email']"],"Pass_in":[(By.ID,"password"),"[id='password']"],"Submit":[(By.CLASS_NAME,"btn-primary"),"text=submit"],
              "Register":[(By.CSS_SELECTOR,"#root > div > button"),"text=Register!"],"FirstNm":[(By.ID,"firstName"),"[id='firstName']"],
              "LastNm":[(By.ID,"lastName"),"[id='lastName']"],}

    def sendLoginData(self,email:str,passw:str):
        email_element=self.getElement(self.locators.get("Email_in"),None,email)
        self.getElement(self.locators.get("Pass_in"),None,passw)
        self.getElement(self.locators.get("Submit"), None, None, "click")
        return self.getAttr(email_element,"validationMessage")


    def submit(self):
        self.getElement(self.locators.get("Submit"), None, None, "click")

    def RegisterOrBackToLogin(self):
        self.getElement(self.locators.get("Register"),None,None,"click")

    def sendRegisterData(self,firstName:str,lastName:str):
        self.getElement(self.locators.get("FirstNm"),None,firstName)
        self.getElement(self.locators.get("LastNm"), None, lastName)

