import pytest
from Pages import AuthorPage,StorePg,LoginPg,MainPage

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
    ap.getFrameContent()




