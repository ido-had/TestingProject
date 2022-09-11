import pytest
from Models.Accounts import *
from Models.Authors import *
from Models.Books import *
import logging
from Tests.Config.swagr_fixtures import user,login,author

@pytest.mark.usefixtures("getAccountApi")
@pytest.mark.usefixtures("loginNewUser")
@pytest.mark.usefixtures("getAuthorApi")
@pytest.mark.usefixtures("getBooksApi")
@pytest.mark.usefixtures("authorInserted")
@pytest.mark.usefixtures("newBook")
@pytest.mark.usefixtures("insertNewBook")

@pytest.mark.valid
@pytest.mark.sanity
def testRegister(getAccountApi):
    res=getAccountApi.postRegister(user)
    assert "DuplicateUserName" in res
    logging.info(res)
    res=getAccountApi.postLogin(login)
    if type(res)!=AuthResponseDto:
        logging.info(res)
    assert type(res)==AuthResponseDto


@pytest.mark.valid
@pytest.mark.sanity
def testLogin(getAccountApi):
    res=getAccountApi.postLogin(login)
    if type(res)!=AuthResponseDto:
        logging.info(res)
    assert type(res) == AuthResponseDto
    assert res._userId
    assert res._token

@pytest.mark.valid
@pytest.mark.sanity
def testRfrshLgn(getAccountApi,loginNewUser):
    res=getAccountApi.postRefreshToken(loginNewUser)
    if type(res)!=AuthResponseDto:
        logging.info(res)

    assert type(res) == AuthResponseDto
    assert res._userId
    assert res._token

@pytest.mark.valid
@pytest.mark.sanity
def testGetAuthors(getAuthorApi):
    res=getAuthorApi.getAuthors()
    if type(res)!=list or len(res)==0:
        logging.info(res)
    assert type(res)==list
    assert len(res)>0

@pytest.mark.valid
@pytest.mark.sanity
def testPostAuthors(getAuthorApi):
    res=getAuthorApi.postAuthors(author)
    if type(res)!=AuthorDto:
        logging.info(res)
    assert type(res)==AuthorDto
    assert res._name==author._name
    assert res._homeLatitude ==author._homeLatitude
    res=getAuthorApi.getAuthors()
    found=False
    for autr in res:
        if author._name==autr._name and author._homeLatitude==autr._homeLatitude:
            found=True
    assert found

@pytest.mark.valid
@pytest.mark.sanity
def testGetAuthorById(getAuthorApi,authorInserted):
    res=getAuthorApi.getById(authorInserted.id)
    if type(res)!=AuthorDto:
        logging.info(res)
    assert res==authorInserted

@pytest.mark.valid
@pytest.mark.sanity
def testUpdateAuthorById(getAuthorApi,authorInserted):
    authorInserted._name="changed"
    res=getAuthorApi.putById(authorInserted)
    if type(res) != AuthorDto:
        logging.info(res)
    res=getAuthorApi.getById(authorInserted.id)
    assert res._name=="changed"

@pytest.mark.valid
@pytest.mark.sanity
def testDelAuthor(getAuthorApi,authorInserted):
    res=getAuthorApi.delAuthor(authorInserted.id)
    if res != True:
        logging.info(res)
    assert res==True
    res=getAuthorApi.getById(authorInserted.id)
    assert "404" and "Not Found" in res

@pytest.mark.sanity
@pytest.mark.valid
def testSrchAuthorByText(getAuthorApi,authorInserted):
    res=getAuthorApi.getSearchByText(authorInserted._name)
    if type(res)!=list:
        logging.info(res)
    assert type(res)==list
    found=False
    for author in res:
        if authorInserted==author:
            found=True
    assert found

@pytest.mark.sanity
@pytest.mark.valid
def testGetBooks(getBooksApi,insertNewBook):
    res=getBooksApi.getBooks()
    if type(res)!=list:
        logging.info(res)
    assert type(res)==list
    found=False
    for book in res:
        if book==insertNewBook:
            found=True
    assert found

@pytest.mark.sanity
@pytest.mark.valid
def testPostBook(getBooksApi,newBook):
    res=getBooksApi.postBooks(newBook)
    if type(res)!=BookDto:
        logging.info(res)
    assert type(res)==BookDto
    assert res==newBook

@pytest.mark.sanity
@pytest.mark.valid
def testGetBookById(getBooksApi,insertNewBook):
    res=getBooksApi.getBookById(insertNewBook.id)
    if type(res)!=Book:
        logging.info(res)
    assert type(res)==Book
    assert res==insertNewBook

@pytest.mark.sanity
@pytest.mark.valid
def testUpdateBook(getBooksApi,insertNewBook,newBook):
    newBook._name="NewName"
    newBook._price = 999
    res=getBooksApi.putBook(newBook)
    if res!=True:
        logging.info(res)
    assert res==True
    res=getBooksApi.getBookById(newBook.id)
    assert newBook==res

@pytest.mark.sanity
@pytest.mark.valid
def testDelBook(getBooksApi,insertNewBook):
    res=getBooksApi.delBookById(insertNewBook.id)
    if res!=True:
        logging.info(res)
    assert res==True
    res=getBooksApi.getBookById(insertNewBook.id)
    assert "404" and "Not Found" in res

@pytest.mark.sanity
@pytest.mark.valid
def testGetBookByAuthorId(getBooksApi,insertNewBook):
    author_id=insertNewBook._authorId
    res=getBooksApi.getBooksByAuthrId(author_id)
    if type(res)!=list:
        logging.info(res)
    assert type(res)==list
    for book in res:
        assert book._authorId==author_id

@pytest.mark.sanity
@pytest.mark.valid
def testPutPurchaseByBkId(getBooksApi,insertNewBook):
    curr_amount=insertNewBook._amountInStock
    book_id=insertNewBook.id
    res=getBooksApi.putPurchaseByBookId(book_id)
    if type(res)!=BookDto:
        logging.info(res)
    assert type(res)==BookDto
    assert res.id==book_id
    assert res._amountInStock==curr_amount-1


@pytest.mark.sanity
@pytest.mark.invalid
def testSearchAuthorBYText(getAuthorApi):
    res=getAuthorApi.getSearchByText("NoAuthorNamed None")












