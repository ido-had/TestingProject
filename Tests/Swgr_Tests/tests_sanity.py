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

@pytest.mark.sanity
def testRegister(getAccountApi):
    res=getAccountApi.postRegister(user)
    assert "DuplicateUserName" in res
    logging.info(res)
    res=getAccountApi.postLogin(login)
    if type(res)!=AuthResponseDto:
        logging.info(res)
    assert type(res)==AuthResponseDto



@pytest.mark.sanity
def testLogin(getAccountApi):
    res=getAccountApi.postLogin(login)
    if type(res)!=AuthResponseDto:
        logging.info(res)
    assert type(res) == AuthResponseDto
    assert res._userId
    assert res._token


@pytest.mark.sanity
def testRfrshLgn(getAccountApi,loginNewUser):
    res=getAccountApi.postRefreshToken(loginNewUser)
    if type(res)!=AuthResponseDto:
        logging.info(res)

    assert type(res) == AuthResponseDto
    assert res._userId
    assert res._token

@pytest.mark.sanity
def testGetAuthors(getAuthorApi):
    res=getAuthorApi.getAuthors()
    if type(res)!=list or len(res)==0:
        logging.info(res)
    assert type(res)==list
    assert len(res)>0


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

@pytest.mark.sanity
def testGetAuthorById(getAuthorApi,authorInserted):
    res=getAuthorApi.getById(authorInserted.id)
    if type(res)!=AuthorDto:
        logging.info(res)
    assert res==authorInserted

@pytest.mark.sanity
def testUpdateAuthorById(getAuthorApi,authorInserted):
    authorInserted._name="changed"
    res=getAuthorApi.putById(authorInserted)
    if type(res) != AuthorDto:
        logging.info(res)
    res=getAuthorApi.getById(authorInserted.id)
    assert res._name=="changed"

@pytest.mark.sanity
def testDelAuthor(getAuthorApi,authorInserted):
    res=getAuthorApi.delAuthor(authorInserted.id)
    if res != True:
        logging.info(res)
    assert res==True
    res=getAuthorApi.getById(authorInserted.id)
    assert "404" and "Not Found" in res
# def test(getAuthorApi):
#     res=getAuthorApi.getById(100)
#     print(res)









