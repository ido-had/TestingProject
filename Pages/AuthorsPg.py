from Pages.BasePage import BasePg
from selenium.webdriver.common.by import By

class AuthorsPage(BasePg):
    def __init__(self,driver):
        super(AuthorsPage, self).__init__(driver)
    locators={"Author_Container":[(By.CLASS_NAME,"author-container"),"[class='author-container']"],"Btn_Footer":[(By.CLASS_NAME,"card-footer"),
    "[class='card-footer']"],"Author_PgBtn":[(By.CLASS_NAME,"btn"),"[class='btn btn-primary']"],"Author_Title":[(By.CLASS_NAME, "card-title"),
    "[class='card-title h5']"]}

    def getAuthors(self):
        authors=self._driver.getElementS(self.locators.get("Author_Container"))
        author_dict={}
        for author in authors:
            card_footer=self._driver.getElement(self.locators["Btn_Footer"],author)
            author_goto_btn=self._driver.getElement(self.locators["Author_PgBtn"],card_footer)
            author_title=self._driver.getElement(self.locators["Author_Title"],author)
            author_txt=self._driver.getText(author_title)
            author_dict[author_txt]=author_goto_btn
        return author_dict

    def findAuthor(self,author):
        authos=self.getAuthors()
        if authos.get(author)!=None:
            from Pages.AuthorPage import AuthorPage
            authos[author].click()
            return AuthorPage(self._driver)
        return False