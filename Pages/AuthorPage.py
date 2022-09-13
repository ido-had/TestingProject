from Pages.BasePage import BasePg
from selenium.webdriver.common.by import By
import re

class AuthorPage(BasePg):
    def __init__(self,driver,frmWork):
        super(AuthorPage, self).__init__(driver,frmWork)

    locators={"book-container":[(By.CLASS_NAME,"book-container"),"[class='book-container']"],"card-img-top":[(By.CLASS_NAME,"card-img-top"),
    "[class='card-img-top']"],"card-footer":[(By.CLASS_NAME,"card-footer"),"[class='card-footer']"],"card-title":[(By.CLASS_NAME,"card-title"),
    "[class='card-title h5']"],"card-text":[(By.CLASS_NAME,"card-text"),"[class='card-text']"],"Author_Name":[(By.CLASS_NAME,"list-group-item"),
    "[class='list-group-item']"],"iframe":[(By.ID,"iframeId")],"viewlargermap":[(By.CLASS_NAME,"google-maps-link"),"[class='google-maps-link']"],
    "position":[(By.CLASS_NAME,"place-name"),"[class='place-name']"]}

    def getBooks(self):
        books=self.getElementS(self.locators["book-container"])
        books_dict={}
        for book in books:
            card_footer = self.getElement(self.locators["card-footer"], book)#'Price: 50 Left In Stock: 10'
            card_footer_text=self.getText(card_footer)
            lst_content= card_footer_text.split()
            price=int(lst_content[1])
            stock=int(lst_content[5])
            book_title= self.getElement(self.locators["card-title"],book) #'The Hunger Games'
            book_title_text=self.getText(book_title)
            book_desc=self.getElement(self.locators["card-text"],book)#'The Hunger Games is a 2008 dystopian novel by the American writer Suzanne Collins'
            book_desc_text=self.getText(book_desc)
            author_name=self.getElement(self.locators["Author_Name"],book) #'By: Suzanne Collins'
            author_name_text=self.getText(author_name)
            authrNmLst=author_name_text.split()
            author_name=f"{authrNmLst[1]} {authrNmLst[2]}"

