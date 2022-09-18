from Pages.BasePage import BasePg
from Pages.LoginPg import LoginPage
from selenium.webdriver.common.by import By

class RegisterPage(BasePg):
    def __init__(self,driver):
        super(RegisterPage, self).__init__(driver)

    locators={"Register":[(By.CSS_SELECTOR,"#root > div > button"),"text=Back To Login!"],"FirstNm":[(By.ID,"firstName"),"[id='firstName']"],
              "LastNm":[(By.ID,"lastName"),"[id='lastName']"]}

    def BackToLogin(self):
        self._driver.getElement(self.locators.get("Register"),None,None,"click")
        return self.getLoginPage()

    def sendRegisterData(self,firstName:str,lastName:str):
        self._driver.getElement(self.locators.get("FirstNm"),None,firstName)
        self._driver.getElement(self.locators.get("LastNm"), None, lastName)
    def getLoginPage(self):
        from Pages.LoginPg import LoginPage
        logPg = LoginPage(self._driver)
        return logPg
    def submit(self):
        logPg=self.getLoginPage()
        return logPg.submit()

    def getValidationMessage(self):
        logPg = self.getLoginPage()
        return logPg.getValidationMessage()

    def sendLoginData(self, email: str, passw: str):
        logPg=self.getLoginPage()
        logPg.sendLoginData(email,passw)