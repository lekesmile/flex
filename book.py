from datetime import date

class Book:
    all_books = []

    def __init__(self, name:str, author:str, genre:str , year:date):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

        Book.all_books.append(self)


    def older_book(self, book):
        first_book = self.year
        second_book = book.year
        if first_book  < second_book:
            return  f" {self.name} is older, it was published in {self.year}"
          

        elif self.year == book.year:
            return  f" Fluent Python and Norma were published in {book.year}"
        
        else:
            return f"{self.name} and {book.name} have the same education level."

    def books_of_genre(books: list, genre: str):
        for book in Book.all_books:
            print(book.name)
            if book == books:
               return f" {books.name : {books.author}}" 
            else:
                return f" No books found!"
            
    
print('*******************Books created*****************************')  
My_book = Book("Solomon Island", "King James", "Fantazy", date(2024,12,1))  
print(f"{My_book.author}: {My_book.name} ({My_book.year})")
print(f"The genre of the book {My_book.name} is {My_book.genre}")
print('-------------------------------------------------------')
My_book2 = Book("High Adventure", "Edmund Hillary", "autobiography", date(2024,12,1))  
print(f"{My_book2.author}: {My_book2.name} ({My_book2.year})")
print(f"The genre of the book {My_book2.name} is {My_book2.genre}")
print('-------------------------------------------------------')
My_book3 = Book("Fluent Python", "Luciano Ramalho", "programming", date(2020,5,1))  
print(f"{My_book3.author}: {My_book3.name} ({My_book3.year})")
print(f"The genre of the book {My_book3.name} is {My_book3.genre}")
  

print("********************Comparing two books*********************")
first_compare = Book.older_book(My_book, My_book2)
first_compare2 = Book.older_book(My_book, My_book3)
print(f"{first_compare}") 
print(f"{first_compare2}") 


print('***********************Books in Genre***********************')
Book.books_of_genre("Edmund Hillary", "crime")
   




class Checklist:
    def __init__(self, header:str, entries:list):
        self.header = header
        self.entries= entries


class Customer:
    def __init__(self, id:str, balance:float, discount:int):
        self.id = id
        self.balance = balance
        self.discount = discount


class Cable:
    def __init__(self, model:str, length:float, max_speed:int, bidirectional:bool):
        self.model = model
        self.length = length
        self.max_speed  = max_speed
        self.bidirectional = bidirectional
