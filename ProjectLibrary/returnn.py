import json
from add_usr import User
from add_book import Book, Rare_Book, Library

class ReturnSystem:
    def __init__(self, user):
        self.user = user
        self.borrowed_books = []

    def load_borrowed_books(self):
        with open(r'F:\ProjectLibrary\borrow.json', 'r') as json_file:
            for line in json_file:
                borrowed_book = json.loads(line)
                if borrowed_book['username'] == self.user.username:
                    self.borrowed_books.append(borrowed_book)

    def show_borrowed_books(self):
        print("\nBorrowed Books:")
        for i, borrowed_book in enumerate(self.borrowed_books, start=1):
            print(f"{i}. Book Name: {borrowed_book['book_name']}\n   Return Date: {borrowed_book['return_date']}")

    def return_book(self):
        self.show_borrowed_books()
        if not self.borrowed_books:
            print("No borrowed books to return.")
            return

        return_index = int(input("Enter the number of the book you want to return: ")) - 1
        if 0 <= return_index < len(self.borrowed_books):
            returned_book = self.borrowed_books.pop(return_index)
            print(f"Book '{returned_book['book_name']}' returned successfully.")
        else:
            print("Invalid book number.")

    def process_return(self):
        self.load_borrowed_books()
        self.show_borrowed_books()

        if self.borrowed_books:
            return_option = input("Do you want to return a book? (Y/N): ").strip().upper()
            if return_option == 'Y':
                self.return_book()

    def save_updated_borrowed_books(self):
        with open(r'F:\ProjectLibrary\borrow.json', 'w') as json_file:
            for borrowed_book in self.borrowed_books:
                json.dump(borrowed_book, json_file)
                json_file.write('\n')

    def show_thank_you(self):
        print("Thank you for using the return system!")


# if __name__ == "__main__":
#     # Assume the user has already logged in using add.py
#     username = input("Enter your username: ")
#     # Load user information from JSON file
#     with open(r'F:\ProjectLibrary\add.json', 'r') as json_file:
#         for line in json_file:
#             user_data = json.loads(line)
#             if user_data['username'] == username:
#                 user = User(**user_data)

#     return_system = ReturnSystem(user)
#     return_system.process_return()
#     return_system.save_updated_borrowed_books()
#     return_system.show_thank_you()
