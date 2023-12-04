import json
from add_usr import User
from add_book import Book, Rare_Book, Library



class BorrowSystem:
    def __init__(self, user):
        self.user = user
        self.library = Library()
        self.borrowed_books = []

    def show_books(self):
        print("\nAvailable Books:")
        self.library.display_books()

    def lend_book(self):
        book_name = input("Enter the name of the book you want to borrow: ")
        book_id = int(input("Enter the unique ID of the book: "))
        return_date = input("Enter the return date (YYYY-MM-DD): ")

        borrowed_book = {
            "username": self.user.username,
            "book_name": book_name,
            "book_id": book_id,
            "return_date": return_date
        }

        self.borrowed_books.append(borrowed_book)
        print("Book borrowed successfully.")

    def process_borrowing(self):
        self.show_books()

        if self.user.subscribe_months > 0:
            # Subscription user can lend two books at once
            for _ in range(2):
                lend_option = input("Do you want to borrow a book? (Y/N): ").strip().upper()
                if lend_option == 'Y':
                    self.lend_book()
                else:
                    break
        else:
            # Normal user can lend only one book at once
            lend_option = input("Do you want to borrow a book? (Y/N): ").strip().upper()
            if lend_option == 'Y':
                self.lend_book()

    def save_borrowed_books(self):
        with open(r'F:\ProjectLibrary\borrow.json', 'a') as json_file:
            for borrowed_book in self.borrowed_books:
                json.dump(borrowed_book, json_file)
                json_file.write('\n')

    def show_thank_you(self):
        print("Thank you for coming!")


# if __name__ == "__main__":
#     # Assume the user has already logged in using add.py
#     username = input("Enter your username: ")
#     # Load user information from JSON file
#     with open(r'F:\ProjectLibrary\add.json', 'r') as json_file:
#         for line in json_file:
#             user_data = json.loads(line)
#             if user_data['username'] == username:
#                 user = User(**user_data)

#     borrow_system = BorrowSystem(user)
#     borrow_system.process_borrowing()
#     borrow_system.save_borrowed_books()
#     borrow_system.show_thank_you()
