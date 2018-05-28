from api.app import db

try:
    db.create_all()
    print("Database created successfully")
except Exception as exception:
    print(f"Could not create database due to {exception}")
