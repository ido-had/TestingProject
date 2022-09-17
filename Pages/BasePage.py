from playwright.sync_api import Page
from Drivers.SelenDrvr import SelenDrvr
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from Tests.Config.Ui_fixtures import SELENIUM, PLAYWRIGHT
from selenium.webdriver import ActionChains


# SELENIUM = 0
# PLAYWRIGHT = 1


class BasePg():
    def __init__(self, driver:SelenDrvr):
        self._driver = driver
        # self.frameWork = frmwork

    Baselocators = {"Backbtn": [(By.CLASS_NAME, "back"), "has text:BACK"],
                    "BookStorelbl": [(By.CLASS_NAME, "navbar-brand"), "[class=navbar-brand]"],
                    "NavBarLinks": [(By.CLASS_NAME, "nav-link"), "[class='nav-link']"],
                    "Search_Txt": [(By.ID, "searchtext"), "[id='searchtext']"],
                    "Search_Btn": [(By.CLASS_NAME, "btn-outline-success"), "[class='btn btn-outline-success']"],
                    "Log_In":[(By.CLASS_NAME,"btn-primary"),"button:has-text(\"Log Out\")"]}

    # ------------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------------------
    def NavBarMainpg(self):
        book_store_lbl = self._driver.getElement(self.Baselocators.get("BookStorelbl"))
        book_store_lbl.click()
        return self.__returnStorePg()

    def NavBarLogIn(self):
        login = self.getLogInLabel()
        login_txt=self._driver.getText(login)
        login.click()
        if login_txt=="Log In":
            from Pages.StorePg import StorePage
            return StorePage(self._driver)
    def getLogInOutTxt(self):
        login = self.getLogInLabel()
        return self._driver.getText(login)

    def NavBarStore(self):
        nvbar_store = self._driver.getElementS(self.Baselocators.get("NavBarLinks"))
        nvbar_store[0].click()
        return self.__returnStorePg()

    def NavBarAuthors(self):
        nvbar_authors = self._driver.getElementS(self.Baselocators.get("NavBarLinks"))
        nvbar_authors[1].click()
        from Pages.AuthorsPg import AuthorsPage
        return AuthorsPage(self._driver)

    def NavBarSearch(self, search_data):
        self._driver.getElement(self.Baselocators.get("Search_Txt"), None, search_data)
        self._driver.getElement(self.Baselocators.get("Search_Btn"), None, None, "Click")
        return self.__returnStorePg()

    def __returnStorePg(self):
        from Pages.StorePg import StorePage
        return StorePage(self._driver)

    def getTitle(self):
        return self._driver.getTitle()
    def getUrl(self):
        return self._driver.getCurrentUrl()
    def getLogInLabel(self):
        try:
            nv_br_login = self._driver.getElementS(self.Baselocators.get("NavBarLinks"))
            nv_br_login= nv_br_login[2]
        except:
            nv_br_login=self._driver.getElement(self.Baselocators["Log_In"])
        finally:
            return nv_br_login
