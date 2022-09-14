import pytest
from Pages import AuthorPage,StorePg,LoginPg,MainPage
from Models.Books import BookDto
@pytest.mark.usefixtures("getLoginPg")

def test1(getLoginPg):
    getLoginPg.sendLoginData("tttt@sdf.xo","1234")
    getLoginPg.RegisterOrBackToLogin()
    getLoginPg.sendRegisterData("asdas","ssss")
    getLoginPg.NavBarMainpg()
    getLoginPg.NavBarStore()
    getLoginPg.NavBarLogIn()
    getLoginPg.NavBarSearch("horror")
    author_page=getLoginPg.NavBarAuthors()
    author_page.findAuthor("hhh")
    ap=author_page.findAuthor("Suzanne Collins")
    ap.getBooks()
    # ap.getFrameContent()
    storePg= ap.NavBarStore()
    storePg.getBooks()
    storePg.findBook(BookDto(None,"The Hunger Games","The Hunger Games is a 2008 dystopian novel by the American writer Suzanne Collins",
                             50,10,None,None,"Suzanne Collins"))
    storePg.purchaseBook(BookDto(None,"The Hunger Games","The Hunger Games is a 2008 dystopian novel by the American writer Suzanne Collins",
                             50,10,None,None,"Suzanne Collins"))
    storePg.findBook(BookDto(None,"The Hunger Games","The Hunger Games is a 2008 dystopian novel by the American writer Suzanne Collins",
                             50,10,None,None,"Suzanne Collins"))



