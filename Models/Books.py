from Models.BaseModel import baseObj


class Book(baseObj):
    def __init__(self, id: int, name: str, description: str, price: float, amountInStock: int, imageUrl: str,
                 authorId: int):
        self._id = id
        self._name = name
        self._description = description
        self._price = price
        self._amountInStock = amountInStock
        self._imageUrl = imageUrl
        self._authorId = authorId

    @property
    def id(self):
        return self._id

    def __eq__(self, other):
        if self.id==other.id and self._name==other._name and self._description==other._description and self._price==other._price and\
                self._amountInStock==other._amountInStock and self._authorId==other._authorId:
            return True
        else:
            return False



class BookDto(Book):
    def __init__(self, id: int, name: str, description: str, price: float, amountInStock: int, imageUrl: str,
                 authorId: int, author):
        super().__init__(id, name, description, price, amountInStock, imageUrl, authorId)
        self._author = author
