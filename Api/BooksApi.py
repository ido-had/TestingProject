from Api.AccountApi import AccountApi
from Models.Books import *


class BooksApi(AccountApi):
    def __init__(self, url: str, bearer: str, rfrshTkn: str, userId):
        super().__init__(f"{url}api/Books", bearer, rfrshTkn, userId)

    def getBooks(self):
        res = self._session.get(f"{self._url}")
        if res.status_code == 200:
            book_lst = []
            for book in res.json():
                bookObj = Book(**book)
                book_lst.append(bookObj)
            return book_lst
        else:
            return f"{res.status_code},{res.text}"

    def postBooks(self, book: Book,repeated=False):
        book_json=book.to_json()
        res=self._session.post(f"{self._url}",data=book_json)
        if res.status_code==200:
            return BookDto(**res.json())
        elif res.status_code==401:
            if "token expired" in res.text and not repeated:
                self.getNewToken()
                return self.postBooks(book,True)
            else:
                return res.text
        else:
            return f"{res.status_code},{res.text}"


    def getBookById(self, bookId: int):
        res=self._session.get(f"{self._url}/{bookId}")
        if res.status_code==200:
            return Book(res.json())
        else:
            return f"{res.status_code},{res.text}"

    def putBook(self, book: Book,repeated=False):
        bkId= book.id
        book_json=book.to_json()
        res=self._session.put(f"{self._url}/{bkId}",book_json)
        if res.status_code==200 or res.status_code==204:
            return True
        elif res.status_code == 401:
            if "token expired" in res.text and not repeated:
                self.getNewToken()
                return self.putBook(book, True)
            else:
                return res.text
        else:
            return f"{res.status_code},{res.text}"


    def delBookById(self, bookId: int,repeated=False):
        res=self._session.get(f"{self._url}/{bookId}")
        if res.status_code==200:
            return True
        elif res.status_code == 401:
            if "token expired" in res.text and not repeated:
                self.getNewToken()
                return self.delBookById(bookId, True)
            else:
                return res.text
        else:
            return f"{res.status_code},{res.text}"

    def getBooksByAuthrId(self, authrId: int):
        res=self._session.get(f"{self._url}findauthor/{authrId}")
        if res.status_code==200:
            lstBooks=[]
            for book in res.json():
                bokObj=Book(**book)
                lstBooks.append(bokObj)
            return lstBooks
        else:
            return f"{res.status_code},{res.text}"


    def putPurchaseByBookId(self, bookId: int,repeated=False):
        res=self._session.put(f"{self._url}purchase{bookId}")
        if res.status_code==200:
            return Book(**res.json())
        elif res.status_code == 401:
            if "token expired" in res.text and not repeated:
                self.getNewToken()
                return self.putPurchaseByBookId(bookId, True)
            else:
                return res.text
        else:
            return f"{res.status_code},{res.text}"



if __name__ == '__main__':
    import requests
    res=requests.get("http://localhost:7017/api/Books/")
    for b in res.json():
        print(b)