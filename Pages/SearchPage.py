from Pages.BasePage import BasePg
from selenium.webdriver.common.by import By

class SearchPage(BasePg):
    def __init__(self,driver):
        super(SearchPage, self).__init__(driver)

    def getAuthorsAndBooks(self):
        try:
            from Pages.AuthorsPg import AuthorsPage
            authors_page=AuthorsPage(self._driver)
            authors=authors_page.getAuthors()
        except:
            authors=None
        try:
            from Pages.StorePg import StorePage
            store_pg=StorePage(self._driver)
            books=store_pg.getBooks(withBtn=False)
        except:
            books=None
        return authors,books


