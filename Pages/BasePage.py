from playwright.sync_api import Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from Tests.Config.Ui_fixtures import SELENIUM, PLAYWRIGHT
from selenium.webdriver import ActionChains

SELENIUM = 0
PLAYWRIGHT = 1


class BasePg():
    def __init__(self, driver, frmwork):
        self._driver = driver
        self.frameWork = frmwork

    Baselocators = {"Backbtn": [(By.CLASS_NAME, "back"), "has text:BACK"],
                    "BookStorelbl": [(By.CLASS_NAME, "navbar-brand"), "[class=navbar-brand]"],
                    "NavBarLinks": [(By.CLASS_NAME, "nav-link"), "[class='nav-link']"],
                    "Search_Txt": [(By.ID, "searchtext"), "[id='searchtext']"],
                    "Search_Btn": [(By.CLASS_NAME, "btn-outline-success"), "[class='btn btn-outline-success']"]}

    def loadPage(self, url):
        if self.frameWork:
            self._driver.goto(url)
        else:
            self._driver.get(url)

    # def setUrl(self,url):
    #     self._url=
    def getElement(self, locator, element=None, setData: str = None, click: bool = None):
        if element == None:
            caller = self._driver
        else:
            caller = element

        if self.frameWork == SELENIUM:
            curr_element = caller.find_element(*locator[SELENIUM])
            self.setDataOrClick(curr_element, setData, click)
            return curr_element
        else:
            try:
                curr_element = caller.locator(locator[PLAYWRIGHT])
            except:
                curr_element = caller.query_selector(locator[PLAYWRIGHT])
            finally:
                self.setDataOrClick(curr_element, setData, click)
                return curr_element

    def getAttr(self, element, attrName: str):
        if self.frameWork:
            return element.getAttribute(attrName)
        else:
            return element.get_attribute(attrName)

    def setDataOrClick(self, element, setData=None, click=None):
        if setData != None:
            self.sendData(element, setData)
        if click != None:
            element.click()

    def getElementS(self, locator, element=None):
        if element == None:
            caller = self._driver
        else:
            caller = element
        if self.frameWork:
            return caller.query_selector_all(locator[PLAYWRIGHT])
        else:
            return caller.find_elements(*locator[SELENIUM])

    def paintElement(self, element):
        if self.frameWork == PLAYWRIGHT:
            element.evaluate("arguments[0].style.border='2px solid red'")
        else:
            self._driver.execute_script("arguments[0].style.border='2px solid red'", element)

    def wait(self, element=None):
        if self.frameWork:
            self._driver.wait_for_load_state()
        else:
            WebDriverWait(self._driver, 20).until(EC.visibility_of_element_located(element))

    def DragDrop(self, base, dest):
        if self.frameWork:
            base.hover()
            self._driver.mouse.down()
            box = dest.boundingBox()
            self._driver.mouse.move(box.x + box.width / 2, box.y + box.height / 2)
            dest.hover()
            self._driver.mouse.up()
        else:
            actions = ActionChains(self._driver)
            actions.drag_and_drop(base, dest).perform()

    def iFrame(self, frame):
        if self.frameWork:
            pass
        else:
            self._driver.switch_to.frame(frame)

    def sendData(self, element, data):
        if self.frameWork:
            element.type(data)
        else:
            element.send_keys(data)
    def getText(self,element):
        if self.frameWork:
            return element.text_content()
        else:
            return element.text

    # ------------------------------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------------------
    def NavBarMainpg(self):
        book_store_lbl = self.getElement(self.Baselocators.get("BookStorelbl"))
        book_store_lbl.click()
        return self.__returnStorePg()

    def NavBarLogIn(self):
        nv_br_login = self.getElementS(self.Baselocators.get("NavBarLinks"))
        nv_br_login[2].click()
        from Pages.LoginPg import LoginPage
        return LoginPage(self._driver, self.frameWork)

    def NavBarStore(self):
        nvbar_store = self.getElementS(self.Baselocators.get("NavBarLinks"))
        nvbar_store[0].click()
        return self.__returnStorePg()

    def NavBarAuthors(self):
        nvbar_authors = self.getElementS(self.Baselocators.get("NavBarLinks"))
        nvbar_authors[1].click()
        from Pages.AuthorsPg import AuthorsPage
        return AuthorsPage(self._driver, self.frameWork)

    def NavBarSearch(self, search_data):
        self.getElement(self.Baselocators.get("Search_Txt"), None, search_data)
        self.getElement(self.Baselocators.get("Search_Btn"), None, None, "Click")
        return self.__returnStorePg()

    def __returnStorePg(self):
        from Pages.StorePg import StorePage
        return StorePage(self._driver, self.frameWork)


if __name__ == '__main__':
    locators = {"Backbtn": [(By.CLASS_NAME, "back"), "has text:BACK"]}
    print(*locators.get("Backbtn")[0])
