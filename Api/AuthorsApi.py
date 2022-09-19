from Api.AccountApi import AccountApi
from Models.General import ProblemDetails
from Models.Authors import *


class AuthorApi(AccountApi):
    def __init__(self, url: str, bearer: str, rfrshTkn: str, userId):
        super().__init__(None, bearer, rfrshTkn, userId)
        self._url=f"{url}api/Authors"

    def getAuthors(self):
        res = self._session.get(f"{self._url}")
        if res.status_code == 200:
            res_json = res.json()
            authors = []
            for author in res_json:
                authorObj = GetAuthorDto(**author)
                authors.append(authorObj)
            return authors
        else:
            return f"status code:{res.status_code}|details:{res.text}"

    def postAuthors(self, author: CreateAuthorDto):
        author_json = author.to_json()
        res = self._session.post(f"{self._url}", data=author_json)
        if res.status_code == 201:
            return AuthorDto(**res.json())
        else:
            try:
                return ProblemDetails(**res.json())
            except:
                return f"status code:{res.status_code}|details:{res.text}"

    def getById(self, author_id: int):
        res = self._session.get(f"{self._url}/{author_id}")
        if res.status_code == 200:
            return AuthorDto(**res.json())
        else:
            return f"status code:{res.status_code}|details:{res.text}"

    def putById(self, author: GetAuthorDto, repeated: bool = False):
        authorId = author.id
        author_json = author.to_json()
        res = self._session.put(f"{self._url}/{authorId}", data=author_json)
        if res.status_code == 200 or res.status_code == 204:
            try:
                result= AuthorDto(**res.json())
            except:
                result=True
            finally:
                return result
        elif res.status_code<500:
            if "token expired" in res.text and not repeated:
                self.getNewToken()
                return self.putById(author, True)
            else:
                try:
                    return ProblemDetails(**res.json())
                except:
                    return f"status code:{res.status_code}|details:{res.text}"
        else:
            return f"status code:{res.status_code}|details:{res.text}"

    def delAuthor(self, authorId: int, repeated: bool = False):
        res = self._session.delete(f"{self._url}/{authorId}")
        if res.status_code == 200 or res.status_code == 204:
            return True
        elif res.status_code <500:
            if "token expired" in res.text and not repeated:
                self.getNewToken()
                return self.delAuthor(authorId, True)
            else:
                try:
                    return ProblemDetails(**res.json())
                except:
                    return f"status code:{res.status_code}|details:{res.text}"

        else:
            return f"status code:{res.status_code}|details:{res.text}"

    def getSearchByText(self, txt: str):
        res = self._session.get(f"{self._url}/search/{txt}")
        if res.status_code == 200:
                lstAuthor=[]
                for author in res.json():
                    lstAuthor.append(GetAuthorDto(**author))
                return lstAuthor
        else:
            try:
                return ProblemDetails(**res.json())
            except:
                return f"status code:{res.status_code}|details:{res.text}"
