# app.py

import datetime


# Database Connection
import pyodbc
from entities.admin import admin_login
from entities.user import user_login, register_user

# Database Connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-R59TVT0;'
    'DATABASE=LibraryManagementSystem1;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

def main():
    print("Welcome to Library Management System")
    while True:
        print("\nMain Menu")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Register User")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_login(cursor)
        elif choice == "2":
            user_login(cursor)
        elif choice == "3":
            register_user(cursor)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
