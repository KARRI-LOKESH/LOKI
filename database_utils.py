from pymongo import MongoClient

def get_database():
    # Connect to MongoDB (change the URI if using a remote database)
    client = MongoClient("mongodb://localhost:27017/")
    return client['password_manager']  # Use or create the database

def create_collection():
    db = get_database()
    if 'passwords' not in db.list_collection_names():
        db.create_collection('passwords')  # Create collection if it doesn't exist

def store_password(username, hashed_password):
    db = get_database()
    passwords_collection = db['passwords']
    passwords_collection.insert_one({
        "username": username,
        "hashed_password": hashed_password
    })
    print("Password stored securely in MongoDB!")
