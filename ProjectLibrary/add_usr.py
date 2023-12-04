import json
import re

class User:
    def __init__(self, username, email, password, retype_password, subscribe_months=0, credit_card=None, pin=None):
        self.username = username
        self.email = email
        self.password = password
        self.retype_password = retype_password
        self.subscribe_months = subscribe_months
        self.credit_card = credit_card
        self.pin = pin

    def validate_password(self):
        if self.password != self.retype_password:
            return False

        if not (any(char.isnumeric() for char in self.password) and
                any(char.isalpha() for char in self.password) and
                any(char.isupper() for char in self.password) and
                any(char.islower() for char in self.password) and
                any(char in "!@#$%^&*()-_+=[]{}|;:'\",.<>?/" for char in self.password)):
            return False

        return True

    def register(self):
        print("Registration:")
        self.username = input("Enter username: ")
        self.email = input("Enter email: ")
        self.password = input("Enter password: ")
        self.retype_password = input("Retype password: ")
        subscribe_option = input("Do you want to subscribe? (Y/N): ").strip().upper()

        if subscribe_option == 'Y':
            self.subscribe_months = int(input("Enter the number of subscription months (1/6/12): "))
            if self.subscribe_months == 6:
                price = 500
            elif self.subscribe_months == 12:
                price = 950
            else:
                price = self.subscribe_months * 100

            self.credit_card = input("Enter credit card number: ")
            self.pin = input("Enter 4-digit PIN: ")

            print(f"Subscription successful. Total cost: Rs. {price}")
        else:
            self.subscribe_months = 0
            print("User subscribed as a Normal Member.")

        if self.validate_password():
            # Save user information to JSON file
            with open(r'F:\ProjectLibrary\add.json', 'a') as json_file:
                json.dump(vars(self), json_file)
                json_file.write('\n')
            print("Registration successful.")
        else:
            print("Invalid password or passwords do not match.")

    def login(self):
        print("Login:")
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Load user information from JSON file
        with open(r'F:\ProjectLibrary\add.json', 'r') as json_file:
            for line in json_file:
                user_data = json.loads(line)
                if user_data['username'] == username and user_data['password'] == password:
                    print("Login successful.")
                    if user_data.get('subscribe_months'):
                        print(f"Subscription Member - Subscription Months: {user_data['subscribe_months']}")
                    else:
                        print("Normal Member")
                    return

        print("Invalid username or password.")


if __name__ == "__main__":
    user_instance = User("", "", "", "")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            user_instance.register()
        elif choice == '2':
            user_instance.login()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
