# เป้าหมาย: สร้างระบบจัดการข้อมูลหนังสือและสมาชิกในห้องสมุดแบบง่ายๆ

class Book():
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
    def __str__(self):
        return (f"Title: {self.__title}, Auther: {self.__author}, ISBN: {self.__isbn}")
    
    def get_title(self):
        return self.__title 
    def get_author(self):
        return self.__author
    def get_isbn(self):
        return self.__isbn
    
class PhysicalBook(Book):
    def __init__(self, title, author, isbn, location):
        super().__init__(title, author, isbn)
        self.__location = location
    def get_location(self):
        return self.__location
    def __str__(self):
        return (f"Physical Book - Title: {self._Book__title}, Author: {self._Book__author}, ISBN: {self._Book__isbn}, Location: {self.__location}")
    
class Ebook(Book):
    def __init__(self, title, author, isbn, file_size):
        super().__init__(title, author, isbn)
        self.__file_size = file_size
        
    def get_file_size(self):
        return self.__file_size
    def __str__(self):
        return (f"EBook - Title: {self._Book__title}, Author: {self._Book__author}, ISBN: {self._Book__isbn}, File Size: {self.__file_size}MB")
    
class Library():
    def __init__(self):
        self.__books = []
        
    def add_book(self, book):
        self.__books.append(book)
        print(f"Added: {book.get_title()}")
        
    def list_all_book(self):
        print("\n--- Listing All Books ---")
        for b in self.__books:
            print(b.__str__())
            
    def find_book_by_title(self,title):
        print(f"\n--- Searching for '{title} ---")
        for book in self.__books:
            if book.get_title() == title:
                return book
        return None  
     
    def remove_book(self, isbn):
        print(f"removing: {isbn}")
        book_to_remove = None
        for book in self.__books:
            if book.get_isbn() == isbn:
                book_to_remove = book
                break
        if book_to_remove:
            self.__books.remove(book_to_remove)
            return True 
        else:
            return False
        
lb = Library()
pb = PhysicalBook("Harry Potter", "JK Rolling", "a01", "New arrival")
eb = Ebook("Learning Python", "Mor Gemini Ai", "o001", 50)


lb.add_book(pb)
lb.add_book(eb)

lb.list_all_book()
print("-" * 20)

found_book = lb.find_book_by_title("Harry Potter")
if found_book:
    print(f"here is the book: {found_book}")
else:
    print(f"No book found")
remove_book=lb.remove_book("a01")
if remove_book:
    print(f"the book has been removed")
else:
    print(f"the book hasn't been removed")
print("-" * 20)

lb.list_all_book()
print("-" * 20)

