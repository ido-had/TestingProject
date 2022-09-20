import pytest
import logging
from Models.Accounts import *
from Models.General import ProblemDetails

@pytest.mark.usefixtures("getLoginPg")
@pytest.mark.usefixtures("getAccountApi")
@pytest.mark.usefixtures("getAuthorApi")

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



