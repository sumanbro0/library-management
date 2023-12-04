import json

class Book:
    uid_counter = 1

    def __init__(self, book_name, author, published_date, genre, quantity):
        self.book_name = book_name
        self.author = author
        self.published_date = published_date
        self.genre = genre
        self.quantity = quantity
        self.book_id = self.generate_unique_id()

    def generate_unique_id(self):
        uid = Book.uid_counter
        Book.uid_counter += 1
        return uid


class Rare_Book(Book):
    def __init__(self, book_name, author, published_date, genre, quantity, rarity_label):
        super().__init__(book_name, author, published_date, genre, quantity)
        self.rarity_label = rarity_label

    def display_info(self):
        print(f"\nRare Book Information:")
        print(f"Book Name: {self.book_name}\nAuthor: {self.author}\nPublished Date: {self.published_date}\nGenre: {self.genre}\nQuantity: {self.quantity}\nUnique ID: {self.book_id}\nRarity: {self.rarity_label}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name, author, published_date, genre, quantity, rarity_label):
        if rarity_label == 'Y':
            rare_book = Rare_Book(book_name, author, published_date, genre, quantity, "Special")
            self.books.append(rare_book)
        else:
            normal_book = Book(book_name, author, published_date, genre, quantity)
            self.books.append(normal_book)

    def display_books(self):
        for i, book in enumerate(self.books, start=1):
            if isinstance(book, Rare_Book):
                book.display_info()
            else:
                print(f"\nBook {i} Information:")
                print(f"Book Name: {book.book_name}\nAuthor: {book.author}\nPublished Date: {book.published_date}\nGenre: {book.genre}\nQuantity: {book.quantity}\nUnique ID: {book.book_id}")

    def save_books_to_file(self):
        file_path = r'F:\ProjectLibrary\book.json'
        with open(file_path, 'w') as json_file:
            book_data = []
            for book in self.books:
                book_data.append({
                    "book_name": book.book_name,
                    "author": book.author,
                    "published_date": book.published_date,
                    "genre": book.genre,
                    "quantity": book.quantity,
                    "book_id": book.book_id,
                    "rarity_label": getattr(book, 'rarity_label', None)  # Only for Rare_Book instances
                })

            json.dump(book_data, json_file, indent=2)

# # Example usage
# library = Library()

# while True:
#     book_name = input("Enter book name: ")
#     author = input("Enter author: ")
#     published_date = input("Enter published date: ")
#     genre = input("Enter genre: ")
#     quantity = int(input("Enter quantity: "))
#     rarity_label = input("Is this a rare book? (Y/N): ").strip().upper()

#     library.add_book(book_name, author, published_date, genre, quantity, rarity_label)

#     add_another_book = input("Do you want to add another book? (Y/N): ").strip().upper()
#     if add_another_book != 'Y':
#         break

# library.display_books()
# library.save_books_to_file()
