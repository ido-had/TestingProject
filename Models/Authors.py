from Models.BaseModel import baseObj
from Models.Books import Book


class CreateAuthorDto(baseObj):
    def __init__(self, name: str, homeLatitude: float, homeLongitude: float):
        self._name = name
        self._homeLatitude = homeLatitude
        self._homeLongitude = homeLongitude


class GetAuthorDto(CreateAuthorDto):
    def __init__(self, name: str = None, homeLatitude: float = None, homeLongitude: float = None, id: int = None):
        super().__init__(name, homeLatitude, homeLongitude)
        self._id = id

    @property
    def id(self):
        return self._id

    def __eq__(self, other):
        if self.id == other.id and self._name == other._name and self._homeLatitude == other._homeLatitude and self._homeLongitude == other._homeLongitude:
            return True
        else:
            return False


class AuthorDto(GetAuthorDto):
    def __init__(self, id: int, name: str, homeLatitude: float, homeLongitude: float, books: [Book]):
        super().__init__(name, homeLatitude, homeLongitude, id)
        self._books = books



