from Pages.BasePage import BasePg
from selenium.webdriver.common.by import By

class AuthorsPage(BasePg):
    def __init__(self,driver):
        super(AuthorsPage, self).__init__(driver)
    locators={"Author_Container":[(By.CLASS_NAME,"author-container"),"[class='author-container']"],"Btn_Footer":[(By.CLASS_NAME,"card-footer"),
    "[class='card-footer']"],"Author_PgBtn":[(By.CLASS_NAME,"btn"),"[class='btn btn-primary']"],"Author_Title":[(By.CLASS_NAME, "card-title"),
    "[class='card-title h5']"]}

    def getAuthors(self):
        self._driver.wait(self.locators.get("Author_Container"))
        authors=self._driver.getElementS(self.locators.get("Author_Container"))
        authors_list=[]
        for author in authors:
            author_dict = {}
            card_footer=self._driver.getElement(self.locators["Btn_Footer"],author)
            author_goto_btn=self._driver.getElement(self.locators["Author_PgBtn"],card_footer)
            author_title=self._driver.getElement(self.locators["Author_Title"],author)
            author_txt=self._driver.getText(author_title)
            author_dict["name"]=author_txt
            author_dict["button"]=author_goto_btn
            authors_list.append(author_dict)
        return authors_list

    def findAuthor(self,author):
        authors=self.getAuthors()
        for aut in authors:
            if aut["name"]==author:
                return aut
        return None

    def goToAuthorPage(self,author:dict):
        author_dict=self.findAuthor(author)
        if author_dict != None:
            from Pages.AuthorPage import AuthorPage
            btn=author_dict["button"]
            btn.click()
            return AuthorPage(self._driver)