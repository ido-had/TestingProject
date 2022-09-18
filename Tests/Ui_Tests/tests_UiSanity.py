import time

import pytest
from Pages import AuthorPage,StorePg,LoginPg,MainPage
from Models.Books import BookDto
@pytest.mark.usefixtures("getLoginPg")

def test1(getLoginPg):
    getLoginPg.sendLoginData("tttt","1234")
    getLoginPg.getTitle()
    getLoginPg.getLogInLabel()
    getLoginPg.NavBarLogIn()
    getLoginPg.getUrl()
    getLoginPg.submit()
    getLoginPg.getValidationMessage()
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
    ap.getFrameContent()
    storePg= ap.NavBarStore()
    storePg.getBooks()
    storePg.findBook(BookDto(None,"The Hunger Games","The Hunger Games is a 2008 dystopian novel by the American writer Suzanne Collins",
                             50,10,None,None,"Suzanne Collins"))
    storePg.purchaseBook(BookDto(None,"The Hunger Games","The Hunger Games is a 2008 dystopian novel by the American writer Suzanne Collins",
                             50,10,None,None,"Suzanne Collins"))
    storePg.findBook(BookDto(None,"The Hunger Games","The Hunger Games is a 2008 dystopian novel by the American writer Suzanne Collins",
                             50,10,None,None,"Suzanne Collins"))

@pytest.mark.sanity
@pytest.mark.ui
@pytest.mark.valid
def testLoginRegisteredUser(getLoginPg):
    getLoginPg.sendLoginData("admin@sela.co.il","ADMIN")
    storPg=getLoginPg.submit()
    assert "/store" in storPg.getUrl()
    assert "Log Out" in storPg.getLogInOutTxt()

@pytest.mark.sanity
@pytest.mark.ui
@pytest.mark.invalid
def testLoginUnregisteredUser(getLoginPg):
    getLoginPg.sendLoginData("noOne@nomail.il", "not registered")
    storPg = getLoginPg.submit()
    assert "/store" not in storPg.getUrl()
    assert "Log Out" not in storPg.getLogInOutTxt()

@pytest.mark.sanity
@pytest.mark.ui
@pytest.mark.invalid
def testLoginBadMail(getLoginPg):
    getLoginPg.sendLoginData("admin", "")
    getLoginPg.submit()
    msg = getLoginPg.getValidationMessage()
    assert "Please include an '@' in the email address" in msg
    getLoginPg.sendLoginData("admin@","")
    getLoginPg.submit()
    msg=getLoginPg.getValidationMessage()
    assert "Please enter a part following '@'." in msg

@pytest.mark.sanity
@pytest.mark.ui
@pytest.mark.valid
def testRegisterValid(getLoginPg):
    regPg=getLoginPg.Register()
    regPg.sendRegisterData("firstnm","Lastnm")
    regPg.sendLoginData("ValidMail@gmail.com","validPass")
    storPg=regPg.submit()
    assert "/store" in storPg.getUrl()
    assert "Log Out" in storPg.getLogInLabel()


@pytest.mark.sanity
@pytest.mark.ui
@pytest.mark.valid
def testPressOnBookStoreLbl(getLoginPg):
    storePg=getLoginPg.pressBookLbl()
    assert "/store" in storePg.getUrl()
    authorsPg=storePg.NavBarAuthors()
    storePg = authorsPg.pressBookLbl()
    assert "/store" in storePg.getUrl()

@pytest.mark.sanity
@pytest.mark.ui
@pytest.mark.valid
def testNavBar(getLoginPg):
    authorsPg=getLoginPg.NavBarAuthors()
    assert "/authors" in authorsPg.getUrl()
    storePg=authorsPg.NavBarStore()
    assert "/store" in storePg.getUrl()
    loginPg=storePg.NavBarLogIn()
    assert "/store" and "/authors" not in loginPg.getUrl()

@pytest.mark.sanity
@pytest.mark.ui
@pytest.mark.valid
def testSearchPage(getLoginPg):
    search_page=getLoginPg.NavBarSearch("testbook")
    authors,books=search_page.getAuthorsAndBooks()
    assert "/search" in search_page.getUrl()
    assert len(authors)==0 and len (books)==0






