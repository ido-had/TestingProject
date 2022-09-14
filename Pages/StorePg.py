from Pages.BasePage import BasePg
from selenium.webdriver.common.by import By
from Models.Books import BookDto


class StorePage(BasePg):
    def __init__(self, driver):
        super(StorePage, self).__init__(driver)

    locators = {"books-container": [(By.CLASS_NAME, "book-container"), "[class='book-container']"],
                "book_img": [(By.CLASS_NAME, "card-img-top"), "[class='card-img-top']"],
                "book_title": [(By.CLASS_NAME, "card-title"), "[class='card-title h5']"],
                "author": [(By.CLASS_NAME, "list-group-item"), "[class='list-group-item']"],
                "description": [(By.CLASS_NAME, "card-text"), "[class='card-text']"],
                "Price_Stock": [(By.CLASS_NAME, "card-footer"), "[class='card-footer']"],
                "Purchase_btn": [(By.CLASS_NAME, "btn"), "[class='btn btn-primary']"]}

    def getBooks(self, withBtn=True):
        book_container = self._driver.getElementS(self.locators["books-container"])
        books_lst = []
        for book in book_container:
            book_img = self._driver.getElement(self.locators["book_img"], book)
            book_img_src = self._driver.getAttr(book_img, "src")
            book_title = self._driver.getElement(self.locators["book_title"], book)
            book_title_txt = self._driver.getText(book_title)
            price_stock = self._driver.getElement(self.locators["Price_Stock"], book)
            price_stock_text = self._driver.getText(price_stock)
            lst_content = price_stock_text.split()
            price = float(lst_content[1])
            stock_split = lst_content[5].split("P")
            stock = int(stock_split[0])
            book_desc = self._driver.getElement(self.locators["description"], book)
            book_desc_text = self._driver.getText(book_desc)
            author_name = self._driver.getElement(self.locators["author"], book)
            author_name_text = self._driver.getText(author_name)
            authrNmLst = author_name_text.split()
            author_name = f"{authrNmLst[1]} {authrNmLst[2]}"
            # book_obj=BookDto(None,book_title_txt,book_desc_text,price,stock,book_img_src,None,author_name)
            books_dict = {"author": author_name, "description": book_desc_text, "price": price, "stock": stock,
                          "title": book_title_txt}
            if withBtn:
                purchase_btn = self._driver.getElement(self.locators["Purchase_btn"], book)
                books_dict["button"] = purchase_btn
            books_lst.append(books_dict)
        return books_lst

    def findBook(self, book: BookDto):
        books = self.getBooks()
        for b in books:
            if book.name == b["title"] and book.description == b["description"] and book.author == b["author"]:
                return b["button"]
        return False

    def purchaseBook(self,book: BookDto):
        btnPurchase=self.findBook(book)
        self._driver.handleAlert()
        btnPurchase.click()
        alert=self._driver.getAlertMessage()
        return alert
