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

    def run_library_system(self):
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
                
                case _:
                    print("Invalid choice")


Manager().run_library_system()