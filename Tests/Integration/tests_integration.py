import pytest
import logging
from Models.Accounts import *
from Models.General import ProblemDetails
from Models.Authors import *
from Tests.Config.swagr_fixtures import login
import time

@pytest.mark.usefixtures("registerNewUser")
@pytest.mark.usefixtures("getLoginPg")
@pytest.mark.usefixtures("getAccountApi")
@pytest.mark.usefixtures("getAuthorApi")
@pytest.mark.usefixtures("getBooksApi")


@pytest.mark.integration
@pytest.mark.valid
def testIntegrationRegisterUser(getLoginPg,getAccountApi):
    login=ApiUserDto("newEmailregister@new.new","123456","firstname","lastname")
    regPg = getLoginPg.Register()
    regPg.sendRegisterData(login._firstName,login._lastName)
    regPg.sendLoginData(login._email, login._password)
    regPg.submit()
    res=getAccountApi.postLogin(LoginDto(login._email, login._password))
    assert type(res)==AuthResponseDto

@pytest.mark.integration
@pytest.mark.valid
def testIntegrationViewAuthors(getLoginPg,getAuthorApi):
    authorsDb=getAuthorApi.getAuthors()
    authors_Page=getLoginPg.NavBarAuthors()
    authorsUi=authors_Page.getAuthors()
    assert len(authorsUi)==len(authorsDb)
    testAuthor=authorsDb[0]
    autPage=authors_Page.goToAuthorPage(testAuthor._name)
    assert "authorpage" in autPage.getUrl()
    titles=autPage.getTitles()
    assert titles["name"]==testAuthor._name
    map_content=autPage.getFrameContent()
    cordinates=f"{testAuthor._homeLatitude},{testAuthor._homeLongitude}"
    assert cordinates in map_content["directionLink"]
    authors_Page=autPage.NavBarAuthors()
    testAuthor = authorsDb[len(authorsDb)-1]
    autPage = authors_Page.goToAuthorPage(testAuthor._name)
    assert "authorpage" in autPage.getUrl()
    titles = autPage.getTitles()
    assert titles["name"] == testAuthor._name
    map_content = autPage.getFrameContent()
    cordinates = f"{testAuthor._homeLatitude},{testAuthor._homeLongitude}"
    assert cordinates in map_content["directionLink"]


@pytest.mark.integration
@pytest.mark.valid
def testIntegrationSearchAuthor(getLoginPg,getAuthorApi,getBooksApi):
    authorDb=CreateAuthorDto("SearchAuthor",2.2,40.2)
    newAuthodet=getAuthorApi.postAuthors(authorDb)
    book = Book("newBook", "", 10, 10, None, newAuthodet._id)
    getBooksApi.postBooks(book)
    searchPg=getLoginPg.NavBarSearch(authorDb._name)
    resAuthor,resBooks=searchPg.getAuthorsAndBooks()
    found=False
    getAuthorApi.delAuthor(newAuthodet._id)
    for aut in resAuthor:
        if aut["name"]==authorDb._name:
            found=True
    assert found,"new author not found in search page"
    found=False
    for b in resBooks:
        if b["author"]==authorDb._name:
            found=True
    assert found,"new book not found in search"

@pytest.mark.integration
@pytest.mark.valid
def testIntegrationGetBooks(getBooksApi,getLoginPg,getAuthorApi):
    booksDb=getBooksApi.getBooks()
    storePg=getLoginPg.NavBarStore()
    booksUi=storePg.getBooks()
    assert len(booksUi)==len(booksDb)
    bookToSearch=booksDb[0]
    authorOfbook=getAuthorApi.getById(bookToSearch._authorId)
    found=False
    for b in booksUi:
        if bookToSearch._name==b["name"] and bookToSearch._description==b["description"] and b["price"]==bookToSearch._price and\
            b["amountInStock"]==bookToSearch._amountInStock and b["author"]==authorOfbook._name and b["imageUrl"]==bookToSearch._imageUrl:
            found=True
    assert found


@pytest.mark.integration
@pytest.mark.valid
def testIntegStockUpdtafterPurchase(getBooksApi,getLoginPg,getAuthorApi):
    book=getBooksApi.getBooks()
    amount=book[0]._amountInStock
    bookAuthor=getAuthorApi.getById(book[0]._authorId)
    searchBook={"name":book[0]._name,"description":book[0]._description,"author":bookAuthor._name}
    getLoginPg.sendLoginData(login.email,login.password)
    storePg=getLoginPg.submit()
    foundBook=storePg.findBook(searchBook,purchase=True)
    book=getBooksApi.getBookById(book[0]._id)
    curr_amount=book._amountInStock
    book._amountInStock=amount
    getBooksApi.putBook(book)
    assert amount>curr_amount







