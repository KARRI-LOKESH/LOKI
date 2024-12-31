from password_utils import check_password_strength, hash_password
from database_utils import create_collection, store_password

def main():
    create_collection()
    print("Welcome to the Password Strength Checker and Secure Storage (MongoDB)!")
    while True:
        print("\nOptions:")
        print("1. Check password strength")
        print("2. Store a new password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            password = input("Enter a password to check: ")
            print(check_password_strength(password))
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if check_password_strength(password) == "Strong":
                hashed = hash_password(password)
                store_password(username, hashed)
            else:
                print("Password is not strong enough to store.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
