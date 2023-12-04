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
                case "return":
                    self.library.return_books()
                case "select":
                        self.select_student(self.user)
                    
                    
                case "upgrade":
                    self.users_manager.upgrade_user()
                case "return":
                    if self.user:
            
                        self.library.return_books(self.user)
                    else:
                        print("Select User to operate on")
                        self.select_student()

                case "b":
                    if self.user:
                        print(self.user)
                        self.library.borrow_books(self.user)
                    else:
                        print("Select User to operate on")
                        self.select_student()
                case "e":
                    break
                case _:
                    print("Invalid choice")


Manager().run_library_system()