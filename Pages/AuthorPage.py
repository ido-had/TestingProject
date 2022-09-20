import time

from Pages.BasePage import BasePg
from selenium.webdriver.common.by import By
import re

class AuthorPage(BasePg):
    def __init__(self,driver):
        super(AuthorPage, self).__init__(driver)

    locators={"book-container":[(By.CLASS_NAME,"book-container"),"[class='book-container']"],"card-img-top":[(By.CLASS_NAME,"card-img-top"),
    "[class='card-img-top']"],"card-footer":[(By.CLASS_NAME,"card-footer"),"[class='card-footer']"],"card-title":[(By.CLASS_NAME,"card-title"),
    "[class='card-title h5']"],"card-text":[(By.CLASS_NAME,"card-text"),"[class='card-text']"],"Author_Name":[(By.CLASS_NAME,"list-group-item"),
    "[class='list-group-item']"],"iframe":[(By.ID,"iframeId"),"[id='iframeId']"],"viewlargermap":[(By.CLASS_NAME,"google-maps-link"),"[class='google-maps-link']"],
    "position":[(By.CLASS_NAME,"place-desc-large"),"[class='place-name']"],"Get_Direction":[(By.CLASS_NAME,"navigate-link"),"[class='navigate-link']"],
    "author_title":[(By.CLASS_NAME,"badge"),"[class='badge bg-secondary']"],"map_title":[(By.TAG_NAME,"h2"),"[style='text-align: center;']"]}

    def getBooks(self):
        from Pages.StorePg import StorePage
        tmpStrPg=StorePage(self._driver)
        return tmpStrPg.getBooks(withBtn=False)



    def getFrameContent(self):
        res_dict={}
        self._driver.wait(self.locators["iframe"])
        frame_element=self._driver.getElement(self.locators["iframe"])
        res_dict["Url_Map_src"]= self._driver.getAttr(frame_element, "src")
        mapbtn = self._driver.iFrame(frame_element, self.locators["viewlargermap"])
        res_dict["viewmapBtn"]=mapbtn
        self._driver.wait(self.locators["Get_Direction"])
        directions=self._driver.iFrame(frame_element,self.locators["Get_Direction"],"dontswitchagain")
        direction_href=self._driver.getAttr(directions,"href")
        self._driver.switchBackFromIframe()
        res_dict["directionLink"]=direction_href
        res_dict["directionBtn"]=directions
        return res_dict



    def getTitles(self):
        authorName=self._driver.getElement(self.locators["author_title"])
        authorNameTxt=self._driver.getText(authorName)
        map_title=self._driver.getElement(self.locators["map_title"])
        map_title_txt=self._driver.getText(map_title)
        return {"name":authorNameTxt,"mapTitle": map_title_txt}
