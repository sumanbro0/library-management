from datetime import datetime, timedelta
import json
from library import Library
from users import Users


class Manager:
    def __init__(self):
        self.users_manager = Users()
        self.library = Library()
        self.user=''

    def select_student(self):
        user=str(input("Enter your user id: ")).strip()
                   
        u=next((usr for usr in self.users_manager.users if str(usr["user_id"])==user),None) 
        if u:
            self.user=u
    
    def save_reports(self):
        try:
            with open("report.json", 'w') as json_file:
                json.dump(self.users_manager.users, json_file, indent=2)
                print("\nUser information saved to report.json.")

            with open("report.txt", 'w') as txt_file:
                txt_file.write("Library Management System Report\n\n")
                txt_file.write("User Information:\n")
                for user in self.users_manager.users:
                    txt_file.write(f"\nUser ID: {user['user_id']}\n")
                    txt_file.write(f"Name: {user['name']}\n")
                    txt_file.write(f"Borrowed Books:\n")
                    for book in user['books']:
                        txt_file.write(f"  - Book ID: {book['id']}\n")
                        txt_file.write(f"    Book Name: {book['name']}\n")
                        txt_file.write(f"    Borrowed Date: {book['borrowed']}\n")
                    txt_file.write("-" * 30 + "\n")

                txt_file.write("\nBook Information:\n")
                for book in self.library.books:
                    txt_file.write(f"\nBook ID: {book['id']}\n")
                    txt_file.write(f"Book Name: {book['name']}\n")
                    txt_file.write(f"Quantity Available: {book['quantity']}\n")
                    txt_file.write("-" * 30 + "\n")

                print("\nReport.txt generated successfully.")

        except Exception as e:
            print(f"Error saving reports: {e}")

    def view_report(self):
        try:
            with open("report.txt", 'r') as txt_file:
                content = txt_file.read()
                print(content)

        except FileNotFoundError:
            print("Report.txt not found. Please generate a report first.")
        

    def gen_fine_report(self):
        fined_users = []
        for user in self.users_manager.users:
            if user["books"]:
                for book in user["books"]:

                    ######################### for days #############################
                    # borrowed_time = datetime.fromisoformat(book["borrowed"])
                    # due_time = borrowed_time + timedelta(days=1)

                    # if datetime.now() > due_time:
                    #     days_overdue = (datetime.now() - due_time).days
                    #     fine = days_overdue * 5
                    #     user["fine"] = fine
                    #     fined_users.append(user.copy())

                    ######################### for mins(testing) #############################

                    borrowed_time = datetime.fromisoformat(book["borrowed"])
                    due_time = borrowed_time + timedelta(minutes=1)

                    if datetime.now() > due_time:
                        days_overdue = (datetime.now() - due_time).total_seconds()//60
                        fine = days_overdue * 5
                        user["fine"] = fine
                        fined_users.append(user.copy())



        return fined_users

    def save_fined_users_to_file(self, filename):
        fined_users = self.gen_fine_report()
        try:
            with open(filename, 'w') as file:
                json.dump(fined_users, file, indent=2)
            print(f"\nFine report saved to {filename} as JSON.")
        except Exception as e:
            print(f"Error saving fine report: {e}")




    
    def show_help(self):
        print("\nHelp - Library Management System:".center(50,"-"))
        print(" 'au': Adds a new user to the system.")
        print(" 'vu': Displays details of all users.")
        print(" 'su': Displays details of single user.")
        print(" 'ab': Adds books to the library.")
        print(" 'vb': Displays details of all books in the library")
        print(" 'b': Allows a user to borrow a book.")
        print(" 'r': Allows a user to return a borrowed book.")    
        print(" 's': Selects a user to perform actions.")
        print(" 'u': Upgrades a user to a special member.")
        print(" 'h': Displays this help menu.")
        print(" 'e': Exits the system.")
        print(" 'rep': View the entire report.")
        print(" 'fine': View the fine report.")



    def run_library_system(self):
        self.show_help()
        while True:
            choice = input("Enter your choice: ").strip().lower()
            match choice:
                case "au":
                        self.users_manager.add_user()
                case "vu":
                    self.users_manager.view_users()
                case "ab":
                    self.library.add_books()
                case "vb":
                    self.library.show_books()
                case "s":
                    self.select_student(self.user)

                case "su":
                    if self.user:            
                        self.users_manager.show_user(self.user)
                    else:
                        print("Select User to Show detail")
                        self.select_student()
                    
                case "u":
                    self.users_manager.upgrade_user()

                case "r":
                    if self.user:            
                        self.library.return_books(self.user)
                    else:
                        print("Select User to operate on")
                        self.select_student()

                case "b":
                    if self.user:
                        self.library.borrow_books(self.user)
                    else:
                        print("Select User to operate on")
                        self.select_student()
                
                case "e":
                    print("Saving data")
                    self.library.save_books_to_file()
                    self.users_manager.save_users_to_file()
                    print("Exitting...")
                    break
                
                case "h":
                    self.show_help()

                case "rep":
                    self.save_reports()
                    print("Report generated successfully ")

                case "fine":
                    self.save_fined_users_to_file("fined.json")
                    print("Fine Report generated successfully ")

                case _:
                    print("Invalid choice")
                    self.show_help()


Manager().run_library_system()