class User:
    def __init__(self, user_id, full_name, location, phone_number, special_member):
        self.id = user_id
        self.full_name = full_name
        self.location = location
        self.phone_number = phone_number
        self.special_member = special_member


def generate_user_id(users):
    return f"{str(len(users)).zfill(3)}"


def get_user_info():
    full_name = input("Enter \003[1mFull Name: ")
    location = input("Enter \003[1mLocation: ")
    phone_number = input("Enter \003[1mPhone Number: ")

    if phone_number.isdigit() and len(phone_number) == 10:
        phone_number = "+977" + phone_number
    else:
        print("Invalid phone number. Please enter a \003[1m10-digit \003[0mnumber.")
        return None

    special_member = input("Suscribrction member?: ").lower() == 'yes'

    user_id = generate_user_id(users)

    user = User(user_id, full_name, location, phone_number, special_member)

    users.append(user)

    display_user_info(user)


def display_user_info(user):
    print("\nUser Information:")
    print(f"User ID: {user.id}")
    print(f"Full Name: {user.full_name}")
    print(f"Location: {user.location}")
    print(f"Phone Number: {user.phone_number}")
    if user.special_member:
        print("Special Member: *")
    else:
        print("Special Member: No")


users = []

