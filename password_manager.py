import hashlib
import getpass
import random


class PasswordManager:

    def __init__(self):
        self.characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%*()"
        self.password_manager = {}

    
    def validate_password(self, password):

        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return False

        if not any(c.isupper() for c in password):
            print("Password must contain at least one uppercase letter.")
            return False

        if not any(c.islower() for c in password):
            print("Password must contain at least one lowercase letter.")
            return False

        if not any(c.isdigit() for c in password):
            print("Password must contain at least one number.")
            return False

        if not any(c in "!@#$%*()" for c in password):
            print("Password must contain at least one special character.")
            return False

        return True

    
    def generate_password(self, length=12):

        if length < 8:
            print("Password length should be at least 8 characters.")
            return None

        return ''.join(random.choice(self.characters) for _ in range(length))

    
    def create_account(self):

        username = input("Enter your username: ")

        if username in self.password_manager:
            print("Username already exists.")
            return

        choice = input("Generate random password? (yes/no): ").strip().lower()

        if choice == "yes":
            length = int(input("Enter password length (min 8): "))
            password = self.generate_password(length)

            if password:
                print("Generated password:", password)

        else:
            password = getpass.getpass("Enter your password: ")

        if not self.validate_password(password):
            return

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        self.password_manager[username] = hashed_password

        print("Account created successfully!")

    
    def login(self):

        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if username in self.password_manager and self.password_manager[username] == hashed_password:
            print("Login successful!")
        else:
            print("Invalid username or password.")

    
    def main(self):

        while True:

            print("\n====== Password Manager ======")
            print("1. Create Account")
            print("2. Login")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()

            elif choice == "2":
                self.login()

            elif choice == "0":
                print("Exiting Password Manager.")
                break

            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":

    manager = PasswordManager()
    manager.main()