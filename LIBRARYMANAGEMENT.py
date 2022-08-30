class Book:
    book_item = []
    def __init__(self, name, author, publish_date, pages):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0
        Book.book_item.append(self)
        
    @classmethod
    def get_all_books(cls):
        print(len(cls.book_item))
        return cls.book_item
class BookData:
    def __init__(self,book,id):
        self.book = book
        self.id = id

class Catalog:

    def searchByName(self, name):
        for book in Book.get_all_books():
            if book.name == name:
                print("the {} written by {}".format(book.name,book.author))
                return book
        else:
            print("This book will be reserved for you")
            return None

    def searchByAuthor(self, author):
        for book in Book.get_all_books():
            if book.author == author:
                print("Author {1} has written the book {}".format(book.name,book.author))
                return book
        else:
            print("no book found")
            return None
class Rack:
    def __init__(self,size):
        self.rack_table = []
        self.size = size
        self.item_count = 0
        
    def add_book_to_rack(self,book,id):
        book_data = BookData(book,id)
        self.rack_table.append(book_data)
        self.item_count +=1
        print("book added successfully")

    def delete_book_in_rack(self,id):
        for book_data in self.rack_table:
            if book_data.id == id:
                self.rack_table.remove(book_data)
                self.item_count -= 1
                print("deleted successfully")
                break
        else:
            print("cannot find the book")

    def issue_book(self,id):
        for book_data in self.rack_table:
            if book_data.id == id:
                return book_data.book
        else:
            return None

    def display_data_in_rack(self,i):
        print(i,end="")
        if len(self.rack_table) != 0:
            for book_data in self.rack_table:
                print("\t\t",book_data.book.name,"\t",book_data.id)
        else:
            print("\t\t NO BOOKS")

    def add_return_book_to_rack(self,book_data):
        self.rack_table.append(book_data)
        self.item_count +=1
        print("book returned successfully")

class Rack:
    def __init__(self,size):
        self.rack_table = []
        self.size = size
        self.item_count = 0
        
    def add_book_to_rack(self,book,id):
        book_data = BookData(book,id)
        self.rack_table.append(book_data)
        self.item_count +=1
        print("book added successfully")

    def delete_book_in_rack(self,id):
        for book_data in self.rack_table:
            if book_data.id == id:
                self.rack_table.remove(book_data)
                self.item_count -= 1
                print("deleted successfully")
                break
        else:
            print("cannot find the book")

    def issue_book(self,id):
        for book_data in self.rack_table:
            if book_data.id == id:
                return book_data.book
        else:
            return None

    def display_data_in_rack(self,i):
        print(i,end="")
        if len(self.rack_table) != 0:
            for book_data in self.rack_table:
                print("\t\t",book_data.book.name,"\t",book_data.id)
        else:
            print("\t\t NO BOOKS")

    def add_return_book_to_rack(self,book_data):
        self.rack_table.append(book_data)
        self.item_count +=1
        print("book returned successfully")

class Library:
    book_count = 0
    books = []
    rack_dict = {}

    def __init__(self,rack_count,rack_size):
        self.book = None
        self.isbn = 0
        for i in range(rack_count):
            Library.rack_dict.setdefault(i+1,Rack(rack_size))

    def add_book_to_rack(self,book,rack_no,id):
        rack = Library.rack_dict.get(rack_no)
        if rack.size > rack.item_count:
            rack.add_book_to_rack(book,id)
            return True
        else:
            rack = input("rack is full please enter different rack or press q to quit")
            if rack == "q":
                return
            else:
                return self.add_book_to_rack(book,int(rack_no),id)
        
    def delete_book_from_rack(self,rack_no,id):
        rack = Library.rack_dict[rack_no]
        rack.delete_book_in_rack(id)
        Library.rack_dict[rack_no] = rack

    def display_all_data(self):
        print ("Rack number \t data \t           id")
        for i in range(len(Library.rack_dict)):
            rack = Library.rack_dict.get(i+1)
            rack.display_data_in_rack(i+1)

    def search_book_by_name(self,name):
        flag = False
        for i in range(len(Library.rack_dict)):
            rack = Library.rack_dict.get(i+1)
            for book_data in rack.rack_table:
                if book_data.book.name == name:
                    print("Book {} is present in rack no {}".format(name,i+1))
                    flag = True
        else:
            if not flag:
                print("No books found")

    def search_book_by_author(self,name):
        flag = False
        for i in range(len(Library.rack_dict)):
            rack = Library.rack_dict.get(i+1)
            for book_data in rack.rack_table:
                if book_data.book.author == name:
                    print("Book {} written by {} is prsesnt in rack no {}".format(book_data.book.name,name,i+1))
                    flag = True
        else:
            if not flag:
                print("No books found for this author")
            
    def search_book_by_id(self,id):
        for i in range(len(Library.rack_dict)):
            rack = Library.rack_dict[i+1]
            for book_data in rack.rack_table:
                if book_data.id == id:
                    return i
                    
        else:
            return None

    def remove_book_from_rack(self,id):
        rack_number = self.search_book_by_id(id)+1
        rack = None
        if rack_number:
            rack = Library.rack_dict[rack_number]
        if rack:
            rack.delete_book_in_rack(id)
        else:
            print("err")
        

    def issued_book(self,id):
        rack_number = self.search_book_by_id(id)
        rack = Library.rack_dict[rack_number+1]
        book = rack.issue_book(id)
        self.remove_book_from_rack(id)
        print("book has been checkout")
        return book

    def accept_return_book(self,book_data,rack_no):
        rack = Library.rack_dict[rack_no+1]
        if rack.size > rack.item_count:
            rack.add_return_book_to_rack(book_data)
            return True
        else:
            return False

class User:
    def __init__(self, name, location, age):
        self.name = name
        self.location = location
        self.age = age

class Librarian(User):
    def __init__(self,name, location, age, emp_id,library):
        super().__init__(name, location, age)
        self.emp_id = emp_id
        self.library = library
        
    def add_book(self, name, author, publish_date, pages):
        self.book = Book(name, author, publish_date, pages)
        id = input('Enter book id:')
        rack = int(input('Enter rack number:'))
        self.library.add_book_to_rack(self.book,rack,id)
    
    def delete_book(self,id):
        self.library.remove_book_from_rack(id)

    def display_all_book(self):
        self.library.display_all_data()

    def search_book(self):
        print("how you want to search")
        print("1)name\n2)author\n3)id\n4)exit")
        number = int(input("enter your choice: "))
        if number == 1:
            name = input("enter name  :  ")
            self.library.search_book_by_name(name)
        elif number == 2:
            name = input("enter author name  : ")
            self.library.search_book_by_author(name)
        elif number == 3:
            name = int(input("enter id :  "))
            print("Book present in",self.library.search_book_by_id(name)+1)
        else:
            return

class Member(User):
    def __init__(self, name, location, age, student_id,library):
        super().__init__(name, location, age)
        self.student_id = student_id
        self.library = library
        self.books = []

    def display_all_book(self):
        self.library.display_all_data()
    
    def search_book(self):
        print("how you want to search")
        print("1)name\n2)author\n3)id\n4)exit")
        number = int(input("enter your choice: "))
        if number == 1:
            name = input("enter name  :  ")
            self.library.search_book_by_name(name)
        elif number == 2:
            name = input("enter author name  : ")
            self.library.search_book_by_author(name)
        elif number == 3:
            name = int(input("enter id :  "))
            print("Book present in rack number",self.library.search_book_by_id(name)+1)
        else:
            return

    def issue_book(self,id):
        if len(self.books) <= 5:
            book = self.library.issued_book(id)
            if book:
                data = BookData(book,id)
                self.books.append(data)
            else:
                print("no book available")
        else:
            print("only 5 books can be checkout")
    
    def return_book(self):
        print("you have {} books to return select how many you want to return  ".format(len(self.books)))
        self.my_books()
        count = int(input("Enter the value: "))
        if count > len(self.books):
            count = int(input("please enter correct value: ")) 
        print("please select book numbers from 1 to {}".format(len(self.books)))
        number_list = []
        for _ in range(count):
            number_list.append(int(input())-1)
        for book_no in number_list:
            book_data = self.books[book_no]
            for i in range(5):
                if self.library.accept_return_book(book_data,i):
                    self.books.remove(book_data)
                    return

    def my_books(self):
        if len(self.books) != 0:
            print("***BOOKS****")
            for book_data in self.books:
                book = book_data.book
                print("\nBook name {} author {}".format(book.name,book.author))
            print("*********************")
        else:
            print("\n****No BOOKS*****")

import sys

b1 = Book("Invisible Man","Richard","2002",1000)
b2 = Book("Beloved","Kevin","2009",540)
b3 = Book("Lords of year","Peterson","2004",667)
b4 = Book("Ulysses","Smith","2007",532)
b5 = Book("War & peace","Johnson","2001",778)
b6 = Book("HarryPotter","Rossouw","2005",987)
b7 = Book("Spiderman","Tommy","2002",698)
b8 = Book("Batman","Cristopher","2011",888)
b9 = Book("Jokers!!","Benjamin","2013",556)
b10 = Book("Avengers","Hilfiger","2014",442)
b11 = Book("Endgame","Wordsworth","2017",560)
b12 = Book("Hamlet","Williamson","2018",320)
b13 = Book("Middlemarch","Root","2019",427)
b14 = Book("Cricket","Joseph","2020",220)
b15 = Book("2 Nations","Fahad","2021",130)

library = Library(20,20)

print('*******************************************')

library.add_book_to_rack(b1,1,1234)
library.add_book_to_rack(b2,2,3455)
library.add_book_to_rack(b3,3,2211)
library.add_book_to_rack(b4,4,1908)
library.add_book_to_rack(b5,5,111)
library.add_book_to_rack(b6,6,223)
library.add_book_to_rack(b7,7,444)
library.add_book_to_rack(b8,8,3333)
library.add_book_to_rack(b9,9,555)
library.add_book_to_rack(b10,10,666)
library.add_book_to_rack(b11,11,7777)
library.add_book_to_rack(b12,12,8888)
library.add_book_to_rack(b13,13,9999)
library.add_book_to_rack(b14,14,9854)
library.add_book_to_rack(b15,15,3432)
print('*****************************************')
print('Fifteen books are added')

member1 = Member("Usman","Karachi",20,123123,library)
member2 = Member("Ali","",23,123124,library)

print("******** WELCOME TO LIBRARY *********")
print("Please enter \n(1)for Librarian\n(2)for Member\n(3)for Exit\n")
loginstate = int(input())
member = None

profile_number = 1
if loginstate == 2:
    print("please choose profile\n 1)Usman 2)Ali")
    profile_number = int(input())
    if profile_number == 1 :
        member = member1
    elif profile_number == 2 :
        member = member2
loggedin = False
while(True):
    
    if loginstate == 1:
        
        
        if(not loggedin):
            print("Enter name and password")
            name = input("Username :")
            password = input("Password :")
            if name == "admin" and password == "admin":
                loggedin = True
                librarian = Librarian(name,"Karachi",25,12345,library)
                continue
        elif loggedin:
            print("please choose any one option")
            print("1) add Book\n2) Delete Book\n3) Display all books\n4) Search book\n5) Exit")
            selected = int(input("Enter "))
            if selected == 1:
                print("enter book details")
                name = input("name :")
                author = input("author :")
                publishdate = input("Publish date :")
                pages = int(input("pages :"))
                librarian.add_book(name,author,publishdate,pages)
                continue
            elif selected == 2:
                librarian.display_all_book()
                id = int(input("enter id number (integer)  "))
                librarian.delete_book(id)
                continue
            elif selected == 3:
                librarian.display_all_book()
                continue
            elif selected == 4:
                librarian.search_book()
                continue
            elif selected == 5:
                exit(0)
            else:
                continue
    
    if loginstate == 2:
        
        print("please choose any one option")
        print("1) search Book\n2) checkout Book\n3) return books\n4) display all book\n5) See my Books\n6) Reserve book\n7) Exit")
        user_choice = int(input("enter value : "))
        if user_choice not in [1,2,3,4,5,6,7]:
            print("please enter valid choice")
            continue
        if user_choice == 1:
            member.search_book()
            continue
        elif user_choice == 2 :
            member.display_all_book()
            print("please choose book : ")
            id = int(input("enter id number : "))
            member.issue_book(id)
            continue
        elif user_choice == 3:
            member.return_book()
            continue
        elif user_choice == 4:
            member.display_all_book()
            continue
        elif user_choice == 5:
            member.my_books()
        elif user_choice==6:
            input('Enter book name which you want to reserve.')
            print('This book will be reserved for you:')
            continue
        elif user_choice==7:
            sys.exit()
    else:
        sys.exit()
