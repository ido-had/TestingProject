import pytest
from Models.Accounts import *
from Models.Authors import *
from Models.Books import *
import logging
from Tests.Config.swagr_fixtures import user,login,author

@pytest.mark.usefixtures("getAccountApi")
@pytest.mark.usefixtures("loginNewUser")




@pytest.mark.valid
@pytest.mark.sanity
def testRegister(getAccountApi):
    res=getAccountApi.postRegister(user)
    assert "DuplicateUserName" in res
    logging.info(res)
    res=getAccountApi.postLogin(login)

    logging.info(res)
    assert type(res)==AuthResponseDto


@pytest.mark.valid
@pytest.mark.sanity
def testLogin(getAccountApi):
    res=getAccountApi.postLogin(login)

    logging.info(res)
    assert type(res) == AuthResponseDto
    assert res._userId
    assert res._token

@pytest.mark.valid
@pytest.mark.sanity
def testRfrshLgn(getAccountApi,loginNewUser):
    res=getAccountApi.postRefreshToken(loginNewUser)

    logging.info(res)

    assert type(res) == AuthResponseDto
    assert res._userId
    assert res._token

@pytest.mark.usefixtures("getAuthorApi")
@pytest.mark.usefixtures("authorInserted")
@pytest.mark.valid
@pytest.mark.sanity
def testGetAuthors(getAuthorApi):
    res=getAuthorApi.getAuthors()

    logging.info(res)
    assert type(res)==list
    assert len(res)>0

@pytest.mark.valid
@pytest.mark.sanity
def testPostAuthors(getAuthorApi):
    res=getAuthorApi.postAuthors(author)

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

    logging.info(res)
    assert res==authorInserted

@pytest.mark.valid
@pytest.mark.sanity
def testUpdateAuthorById(getAuthorApi,authorInserted):
    prevName=authorInserted._name
    authorInserted._name="changed"
    res=getAuthorApi.putById(authorInserted)

    logging.info(res)
    res=getAuthorApi.getById(authorInserted.id)
    assert res._name=="changed"
    authorInserted._name=prevName
    getAuthorApi.putById(authorInserted)


@pytest.mark.valid
@pytest.mark.sanity
def testDelAuthor(getAuthorApi,authorInserted):
    res=getAuthorApi.delAuthor(authorInserted.id)

    logging.info(res)
    assert res==True
    res=getAuthorApi.getById(authorInserted.id)
    assert "404" and "Not Found" in res

@pytest.mark.sanity
@pytest.mark.valid
def testSrchAuthorByText(getAuthorApi,authorInserted):
    res=getAuthorApi.getSearchByText(authorInserted._name)

    logging.info(res)
    assert type(res)==list
    found=False
    for author in res:
        if authorInserted._name in author.__str__():
            found=True
    assert found
@pytest.mark.usefixtures("getBooksApi")
@pytest.mark.usefixtures("newBook")
@pytest.mark.usefixtures("insertNewBook")
@pytest.mark.sanity
@pytest.mark.valid
def testGetBooks(getBooksApi,insertNewBook):
    res=getBooksApi.getBooks()

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

    logging.info(res)
    assert type(res)==BookDto
    assert res==newBook

@pytest.mark.sanity
@pytest.mark.valid
def testGetBookById(getBooksApi,insertNewBook):
    res=getBooksApi.getBookById(insertNewBook.id)

    logging.info(res)
    assert type(res)==BookInserted
    assert res==insertNewBook

@pytest.mark.sanity
@pytest.mark.valid
def testUpdateBook(getBooksApi,insertNewBook):
    insertNewBook._name="NewName"
    insertNewBook._price = 999
    res=getBooksApi.putBook(insertNewBook)

    logging.info(res)
    assert res==True
    res=getBooksApi.getBookById(insertNewBook.id)
    assert insertNewBook==res

@pytest.mark.sanity
@pytest.mark.valid
def testDelBook(getBooksApi,insertNewBook):
    res=getBooksApi.delBookById(insertNewBook.id)

    logging.info(res)
    assert res==True
    res=getBooksApi.getBookById(insertNewBook.id)
    assert "404" and "Not Found" in res

@pytest.mark.sanity
@pytest.mark.valid
def testGetBookByAuthorId(getBooksApi,insertNewBook):
    author_id=insertNewBook._authorId
    res=getBooksApi.getBooksByAuthrId(author_id)

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

    logging.info(res)
    assert type(res)==BookDto
    assert res.id==book_id
    assert res._amountInStock==curr_amount-1


@pytest.mark.sanity
@pytest.mark.invalid
def testSearchAuthorBYText(getAuthorApi):
    res=getAuthorApi.getSearchByText("NoAuthorNamed None")
    pass












