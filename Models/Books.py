from Models.BaseModel import baseObj


class Book(baseObj):
    def __init__(self, name: str, description: str, price: float, amountInStock: int, imageUrl: str,
                 authorId: int):

        self._name = name
        self._description = description
        self._price = price
        self._amountInStock = amountInStock
        self._imageUrl = imageUrl
        self._authorId = authorId



    def __eq__(self, other):
        if  self._name==other._name and self._description==other._description and self._price==other._price and\
                self._amountInStock==other._amountInStock and self._authorId==other._authorId:
            return True
        else:
            return False

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description


class BookInserted(Book):
    def __init__(self, id:int, name: str, description: str, price: float, amountInStock: int, imageUrl: str,
                 authorId: int):
        self._id = id
        super().__init__(name, description, price, amountInStock, imageUrl, authorId)

    @property
    def id(self):
        return self._id

    def __eq__(self, other):
        if super().__eq__(other) == True :
            return True
        return False
class BookDto(Book):
    def __init__(self, id:int, name: str, description: str, price: float, amountInStock: int, imageUrl: str,
                 authorId: int, author:str):
        self._id = id
        self._author = author
        super().__init__( name, description, price, amountInStock, imageUrl, authorId)


    @property
    def id(self):
        return self._id

    def __eq__(self, other):
        if super().__eq__(other)==True :
            return True
        return False

    @property
    def author(self):
        return self._author




