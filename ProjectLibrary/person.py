class Person:
    unique_id_counter = 0

    def __init__(self):
        self.name = input("Enter name: ")
        self.address = input("Enter address: ")

        try:
            phone_number = input("Enter phone number: +977")
            if len(phone_number) != 10 or not phone_number.isdigit():
                raise ValueError("Phone number must be a 10-digit number.")
            self.phone_number = "+977" + phone_number
        except ValueError as ve:
            print(f"Error: {ve}")

        self.unique_id = self.generate_unique_id()

    def generate_unique_id(self):
        unique_id = format(Person.unique_id_counter, '03d')
        Person.unique_id_counter += 1
        return unique_id


class SuperMember(Person):
    def __init__(self, super_member_info):
        super().__init__()

        self.super_member = super_member_info
        self.users = []
        self.subs_users = []

    def check_subscription(self):
        subscription_info = input("Is the person a subscription member? (Y/N): ").strip().upper()
        if subscription_info == 'Y':
            subs_user = SuperMember(subscription_info)
            self.users.append(subs_user)
            self.subs_users.append(subs_user)


# Example usage
# Add a person
user = SuperMember(None)
user.check_subscription()

# You can continue adding more users or performing other actions here
