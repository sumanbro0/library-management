import copy
from datetime import datetime, timedelta
import json
import uuid

class Library:
    filename="books.json"
    def __init__(self):
        self.books = []
        self.load_books_from_file()


    def add_books(self):
        try:
            book={"special":0}
            book["id"]=str(uuid.uuid4())
            name=str(input("Enter book name: ")).strip()
            author=str(input("Enter author's name: ")).strip()
            genre=str(input("Enter Genere: ")).strip()
            quantity=int(input("Enter quantity of books: "))
            special_book=input("This book is Special? (t/f) default=f: ")
            if special_book == 't':
                book["special"]=1
            if name and author and genre and quantity:
                book.update({"name":name,"author":author,"genre":genre,"quantity":quantity})
            else:
                print("Every book details are required.")
            self.books.append(book)
        except Exception as e:
            print(f"Error {e}".center(200,"*"))


    def borrow_books(self,user):
        try:
            if (not user["special_member"] and user["borrowed"]<1 ) or (user["special_member"] and user["borrowed"]<2):
                book_tobe_taken=str(input("Enter book id you want to take: ")).strip()
                b=next((book for book in self.books if str(book["id"])==book_tobe_taken),None)
                if b:
                    book_tobe_appended = copy.copy(b)
                    del book_tobe_appended["quantity"]
                    if b["special"] and user["special_member"]:
                            book_tobe_appended["borrowed"]=datetime.now().isoformat()
                            b["quantity"]-=1
                            user["books"].append(book_tobe_appended)
                            user["borrowed"]+=1  
                            return_date=datetime.now()+timedelta(days=5)
                            print(f"Book must be returned within {return_date.isoformat()}")  
                    elif not b["special"]:
                            b["quantity"]-=1
                            book_tobe_appended["borrowed"]=datetime.now().isoformat()
                            user["books"].append(book_tobe_appended)
                            user["borrowed"]+=1  
                            return_date=datetime.now()+timedelta(days=5)
                            print(f"Book must be returned within {return_date.isoformat()}")   
                    else:
                        print("This book is only for Special user Please upgrade to premium plan")
                else:
                    print("Book not found")      
            else:
                print("Books Borrow limit reached... Please return your books to take more")

        except Exception as e:
            print(e)



    def return_books(self,user):
        try:
            book_tobe_rem=str(input("Enter book id you want to return: ")).strip()
            b = next((book for book in user["books"] if book["id"] == book_tobe_rem), None)
            if b:
                removed=False
                for book in self.books:
                    if b["id"]==book["id"]:
                        book["quantity"]+=1
                        removed=True
                        user["books"].remove(b)
                        user['borrowed']-=1
                        break
                if removed:
                    print("Book Returned")
            else:
                print("The book is not present in your profile")
                
                
        except Exception as e:
            print("Book taken not found in your profile")



    def show_books(self):
        
        try:
            print(self.books)
            for book in self.books:
                
                if book["special"]:
                    print("\nSpecial Users Only".center(100,"-"))
                print("\n| {:^40} | {:^20} | {:^20} | {:^10} | {:^30} |\n".format(
                    book["id"],
                    book["name"],
                    book["author"],
                    book["quantity"],
                    book["genre"]
                ))

        

        except Exception as e:
            print(e)

    def save_books_to_file(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.books, file, indent=2)
            print(f"\nBook details saved to {self.filename} as JSON.")
        except Exception as e:
            print(f"Error saving book details: {e}")

    def load_books_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                self.books = json.load(file)
            print(f"\nBook details loaded from {self.filename}.")
        except Exception as e:
            print(f"Error loading book details: {e}")

    