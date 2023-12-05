from datetime import datetime, timedelta
from helpers import  save_to_file
from library import Library
from users import Users
from write_report import write_report


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
            save_to_file("report.json",self.users_manager.users)
            write_report(self.users_manager.users,self.library.books)

        except Exception as e:
            print(f"Error saving reports: {e}")

        

    def gen_fine_report(self):
        fined_users = []
        for user in self.users_manager.users:
            if user["books"]:
                for book in user["books"]:
                    borrowed_time = datetime.fromisoformat(book["borrowed"])
                    due_time = borrowed_time + timedelta(days=15)
                    if datetime.now()+timedelta(days=16) > due_time:
                        
                        user["fine"] = 10*((datetime.now()-due_time).total_seconds()//86400)
                        # user["fine"] = 10*((datetime.now()-due_time).total_seconds()//60)
                        print("fine",user["fine"])
                        fined_users.append(user.copy())
        return fined_users
    


    def save_fined_users_to_file(self):
        fined_users = self.gen_fine_report()
        try:
            save_to_file("fined.json",fined_users)
            print("Fine Report generated successfully ")

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
                    self.select_student()

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
                    save_to_file(self.users_manager.filename,self.users_manager.users)
                    save_to_file(self.library.filename,self.library.books)
                    print("Exitting...")
                    break
                
                case "h":
                    self.show_help()

                case "rep":
                    self.save_fined_users_to_file()
                    self.save_reports()
                    print("Report generated successfully ")


                case _:
                    print("Invalid choice")
                    self.show_help()


Manager().run_library_system()