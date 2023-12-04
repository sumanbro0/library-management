import json
from add import User
from borrow import BorrowSystem
from return_books import ReturnSystem
from book import Book, Rare_Book, Library

class MemberReport:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user = None
        self.borrowed_books = []

    def load_user_info(self):
        with open(r'F:\ProjectLibrary\add.json', 'r') as json_file:
            for line in json_file:
                user_data = json.loads(line)
                if user_data['unique_id'] == self.user_id:
                    self.user = User(**user_data)
                    break

    def load_borrowed_books(self):
        with open(r'F:\ProjectLibrary\borrow.json', 'r') as json_file:
            for line in json_file:
                borrowed_book = json.loads(line)
                if borrowed_book['username'] == self.user.username:
                    self.borrowed_books.append(borrowed_book)

    def load_returned_books(self):
        returned_books = []
        with open(r'F:\ProjectLibrary\borrow.json', 'r') as json_file:
            for line in json_file:
                returned_book = json.loads(line)
                if returned_book['username'] == self.user.username:
                    returned_books.append(returned_book)
        return returned_books

    def show_report(self):
        self.load_user_info()
        if not self.user:
            print("User not found.")
            return

        self.load_borrowed_books()
        returned_books = self.load_returned_books()

        print("\nMember Report:")
        print(f"User Unique ID: {self.user.unique_id}")
        print(f"Username: {self.user.username}")
        print(f"Number of Books Taken: {len(self.borrowed_books)}")

        if self.borrowed_books:
            print("Books Taken:")
            for i, borrowed_book in enumerate(self.borrowed_books, start=1):
                print(f"  {i}. Book Name: {borrowed_book['book_name']}")
                print(f"     Return Date: {borrowed_book['return_date']}")
        else:
            print("No books taken.")

        print(f"\nNumber of Books to be Returned: {len(returned_books)}")

        if returned_books:
            print("Returned Books:")
            for i, returned_book in enumerate(returned_books, start=1):
                print(f"  {i}. Book Name: {returned_book['book_name']}")
                print(f"     Return Date: {returned_book['return_date']}")
        else:
            print("No books returned.")

        print("\nDate of Book Taken: Not implemented in the borrow.json file.")

if __name__ == "__main__":
    # Assume the user has already logged in using add.py and has a unique ID
    user_id = input("Enter the unique ID of the user to show the report: ")
    
    member_report = MemberReport(user_id)
    member_report.show_report()
