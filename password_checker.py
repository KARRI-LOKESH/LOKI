import re
import hashlib
from pymongo import MongoClient

# MongoDB Setup
def get_database():
    # Connect to MongoDB (local server or replace with your MongoDB Atlas URI)
    client = MongoClient("mongodb://localhost:27017/")
    return client['password_manager']  # Database name

def create_collection():
    db = get_database()
    if 'passwords' not in db.list_collection_names():
        db.create_collection('passwords')  # Create collection if not exists

def store_password(username, hashed_password):
    db = get_database()
    passwords_collection = db['passwords']
    passwords_collection.insert_one({
        "username": username,
        "hashed_password": hashed_password
    })
    print("Password stored securely in MongoDB!")

# Password Strength Checker
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Weak: Password must include at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Weak: Password must include at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Weak: Password must include at least one digit."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password must include at least one special character."
    return "Strong"

# Hashing Passwords
def hash_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

# Main Program
def main():
    create_collection()  # Ensure the MongoDB collection exists
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
