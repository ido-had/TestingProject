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
    "[class='list-group-item']"],"iframe":[(By.ID,"iframeId"),"[id='root']"],"viewlargermap":[(By.CLASS_NAME,"google-maps-link"),"[class='google-maps-link']"],
    "position":[(By.CLASS_NAME,"place-desc-large"),"[class='place-name']"]}

    def getBooks(self):
        from Pages.StorePg import StorePage
        tmpStrPg=StorePage(self._driver)
        return tmpStrPg.getBooks(withBtn=False)
        # books=self._driver.getElementS(self.locators["book-container"])
        # books_lst=[]
        # for book in books:
        #     card_footer = self._driver.getElement(self.locators["card-footer"], book)#'Price: 50 Left In Stock: 10'
        #     card_footer_text=self._driver.getText(card_footer)
        #     lst_content= card_footer_text.split()
        #     price=int(lst_content[1])
        #     stock=int(lst_content[5])
        #     book_title= self._driver.getElement(self.locators["card-title"],book) #'The Hunger Games'
        #     book_title_text=self._driver.getText(book_title)
        #     book_desc=self._driver.getElement(self.locators["card-text"],book)#'The Hunger Games is a 2008 dystopian novel by the American writer Suzanne Collins'
        #     book_desc_text=self._driver.getText(book_desc)
        #     author_name=self._driver.getElement(self.locators["Author_Name"],book) #'By: Suzanne Collins'
        #     author_name_text=self._driver.getText(author_name)
        #     authrNmLst=author_name_text.split()
        #     author_name=f"{authrNmLst[1]} {authrNmLst[2]}"
        #     books_dict={}
        #     books_dict["author"]=author_name
        #     books_dict["description"]=book_desc_text
        #     books_dict["price"]=price
        #     books_dict["stock"]=stock
        #     books_dict["title"]=book_title_text
        #     books_lst.append(books_dict)
        # return books_lst


    def getFrameContent(self):
        res_dict={}
        self._driver.wait(self.locators["iframe"])
        frame_element=self._driver.getElement(self.locators["iframe"])
        res_dict["Posi_str"]= self._driver.getAttr(frame_element, "src")
        mapbtn=self._driver.iFrame(frame_element,self.locators["viewlargermap"])
        res_dict["largermapBtn"]=mapbtn
        # pos=self._driver.iFrame(frame_element,self.locators["position"],"dontswitchagain")
        # txt=self._driver.getText(pos)
        return res_dict



#//*[@id="mapDiv"]/div/div/div[4]/div/div/div/div/div[1]
