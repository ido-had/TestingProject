from Api.AccountApi import AccountApi
from Models.Authors import *


class AuthorApi(AccountApi):
    def __init__(self, url: str, bearer: str, rfrshTkn: str, userId):
        super().__init__(f"{url}api/", bearer, rfrshTkn, userId)

    def getAuthors(self):
        res = self._session.get(f"{self._url}Authors")
        if res.status_code == 200:
            res_json = res.json()
            authors = []
            for author in res_json["Authors"]:
                authorObj = GetAuthorDto(**author)
                authors.append(authorObj)
            return authors
        else:
            return res.status_code

    def postAuthors(self, author: CreateAuthorDto):
        author_json = author.to_json()
        res = self._session.post(f"{self._url}Authors", data=author_json)
        if res.status_code == 200:
            return AuthorDto(**res.json())
        elif res.status_code == 401:
            return res.text
        else:
            return res.status_code

    def getById(self, author_id: int):
        res = self._session.get(f"{self._url}Authors/{author_id}")
        if res.status_code == 200:
            return AuthorDto(**res.json())
        elif res.status_code == 401:
            return res.text
        else:
            return res.status_code

    def putById(self, author: GetAuthorDto, repeated: bool = False):
        authorId = author.id
        author_json = author.to_json()
        res = self._session.put(f"{self._url}Authors/{authorId}", data=author_json)
        if res.status_code == 200 or res.status_code == 204:
            return AuthorDto(**res.json())
        elif res.status_code == 401:
            if "token expired" in res.text and not repeated:
                self.getNewToken()
                return self.putById(author, True)
            else:
                return res.text
        else:
            return res.status_code

    def delAuthor(self, authoId: int, repeated: bool = False):
        res = self._session.delete(f"{self._url}Authors/{authoId}")
        if res.status_code == 200 or res.status_code == 204:
            return True
        elif res.status_code == 401:
            if "token expired" in res.text and not repeated:
                self.getNewToken()
                return self.delAuthor(authoId, True)
            else:
                return res.text
        else:
            return res.status_code

    def getSearchByText(self, txt: str):
        res = self._session.get(f"{self._url}Authors/search/{txt}")
        if res.status_code == 200:
            if len(res.json()) > 0:
                return GetAuthorDto(**res.json())
            else:
                return GetAuthorDto()
        else:
            return res.text
