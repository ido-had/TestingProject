from Api.baseApi import baseApi
from Models.Authors import *

class AuthorApi(baseApi):
    def __init__(self,url,header):
        super().__init__(f"{url}api/",header)

    def getAuthors(self):
        res=self._session.get(f"{self._url}Authors")
        if res.status_code==200:
            res_json=res.json()
            authors=[]
            for author in res_json["Authors"]:
                authorObj=GetAuthorDto(**author)
                authors.append(authorObj)
            return authors
        else:
            return res.status_code
    def postAuthors(self,author:CreateAuthorDto):
        author_json=author.to_json()
        res=self._session.post(f"{self._url}Authors",data=author_json)
        if res.status_code==200:
            return AuthorDto(**res.json())
        elif res.status_code==401:
            return res.text
        else:
            return res.status_code
    def getById(self,id:int):
        res = self._session.get(f"{self._url}Authors/{id}")
        if res.status_code == 200:
            return AuthorDto(**res.json())
        elif res.status_code == 401:
            return res.text
        else:
            return res.status_code

    def putById(self,author:GetAuthorDto):
        id= author.id
        author_json=author.to_json()
        res = self._session.put(f"{self._url}Authors/{id}",data=author_json)
        if res.status_code==200:
            return AuthorDto(**res.json())
        elif res.status_code == 401:
            return res.text
        else:
            return res.status_code

    def delAuthor(self,id:int):
        res = self._session.delete(f"{self._url}Authors/{id}")
        if res.status_code == 200:
            return True
        elif res.status_code == 401:
            return res.text
        else:
            return res.status_code
    def getSearchByText(self,txt:str):
        res = self._session.get(f"{self._url}Authors/search/{txt}")
        if res.status_code==200:
            if len(res.json())>0:
                return GetAuthorDto(**res.json())
            else:
                return GetAuthorDto()
        else:
            return res.text
