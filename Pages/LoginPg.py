import time

from Pages.BasePage import BasePg
from selenium.webdriver.common.by import By

class LoginPage(BasePg):
    def __init__(self,driver):
        super(LoginPage, self).__init__(driver)
    locators={"Email_in":[(By.ID,"email"),"#email"],"Pass_in":[(By.ID,"password"),"[id='password']"],"Submit":[(By.CLASS_NAME,"btn-primary"),"text=submit"],
              "Register":[(By.CSS_SELECTOR,"#root > div > button"),"text=Register!"],"FirstNm":[(By.ID,"firstName"),"[id='firstName']"],
              "LastNm":[(By.ID,"lastName"),"[id='lastName']"]}

    def sendLoginData(self,email:str,passw:str):
        email_element=self._driver.getElement(self.locators.get("Email_in"),None,email)
        self._driver.getElement(self.locators.get("Pass_in"),None,passw)
        # self._driver.getElement(self.locators.get("Submit"), None, None, "click")

    def getValidationMessage(self):
        email=self._driver.getElement(self.locators.get("Email_in"))
        return self._driver.executeScript("document.querySelector('#email').validationMessage;",email)


    def submit(self):
        self._driver.getElement(self.locators.get("Submit"), None, None, "click")
        from Pages.StorePg import StorePage
        time.sleep(1)
        return StorePage(self._driver)

    def Register(self):
        self._driver.getElement(self.locators.get("Register"),None,None,"click")
        from Pages.RegisterPage import RegisterPage
        return RegisterPage(self._driver)

    # def sendRegisterData(self,firstName:str,lastName:str):
    #     self._driver.getElement(self.locators.get("FirstNm"),None,firstName)
    #     self._driver.getElement(self.locators.get("LastNm"), None, lastName)

