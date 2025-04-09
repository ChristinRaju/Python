class Admin:
    def __init__(self, email, username, password):
        self._email = email          # Protected
        self.username = username     # Public
        self.__password = password   # Private

    def login(self, password):
        if password == self.__password:
            print("Admin login successful.")
        else:
            print("Admin login failed.")

    def display_details(self):
        print("Email:", self._email)
        print("Username:", self.username)
        print("Password: [Hidden]")


class Engineer(Admin):
    def __init__(self, email, username):
        super().__init__(email, username, "")  # Password not needed

    def display_details(self):
        print("Email:", self._email)
        print("Username:", self.username)


class User:
    def __init__(self, username):
        self.username = username

    def display_details(self):
        print("Username:", self.username)
        print("No access to email or password.")


print("=== Admin ===")
admin1 = Admin("admin@company.com", "admin123", "securepass")
admin1.display_details()
admin1.login("securepass")

print("\n=== Engineer ===")
engineer1 = Engineer("engineer@company.com", "eng007")
engineer1.display_details()

print("\n=== User ===")
user1 = User("user001")
user1.display_details()
