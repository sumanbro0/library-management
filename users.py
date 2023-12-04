import uuid

class Users:
    def __init__(self):
        self.users = []

    def add_user(self):
        try:
            name = str(input("Enter the name: ")).strip()
            address = str(input("Enter the address: ")).strip()
            phone_number = int(input("Enter the phone number (unique): ")).strip()

            if not name or not address or not phone_number:
                raise ValueError("Name, address, and phone number are required.")

            if any(user['phone_number'] == phone_number for user in self.users):
                raise ValueError(f"User with phone number '{phone_number}' already exists.")

            user_dict = {
                'user_id': str(uuid.uuid4()),
                'name': name,
                'address': address,
                'phone_number': phone_number,
                'books': [],
                'borrowed': 0,
                'special_member': False
            }

            self.users.append(user_dict)
            print(f"\nUser '{name}' added successfully with user ID: {user_dict['user_id']}")

        except ValueError as e:
            print(f"Error: {e}")

    def view_users(self):
        if not self.users:
            print("\nNo users available.")
        else:
            print("\nUser Details:")
            for user in self.users:
                print("\n".join(f"{key}: {value}" for key, value in user.items()))
                print('-' * 20)

    def remove_user(self):
        try:
            phone_number = input("Enter the phone number of the user to be removed: ").strip()

            if not phone_number:
                raise ValueError("Phone number is required.")

            user_to_remove = next((user for user in self.users if user.get('phone_number') == phone_number), None)

            if user_to_remove:
                self.users.remove(user_to_remove)
                print(f"\nUser with phone number '{phone_number}' removed successfully.")
            else:
                print(f"\nUser with phone number '{phone_number}' not found.")

        except ValueError as e:
            print(f"Error: {e}")

    def upgrade_user(self):
        try:
            uid = str(input("Enter Your User id: ")).strip()
            usr=[user for user in self.users if uid==str(user["user_id"])][0]
            if not usr["special_member"]:
                usr["special_member"]=True
                print("User Upgraded")
            else:
                print("User already a special member")
            
        except Exception as e:
            print("User not found")

    def save_users_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for user in self.users:
                    file.write(str(user) + '\n')

            print(f"\nUser details saved to {filename}.")

        except Exception as e:
            print(f"Error saving user details to file: {e}")