# entities/user.py

import pyodbc
import datetime
from entities.search import search_books_by_title,search_books_by_author
from entities.book import display_books
from entities.update import rent_book_user

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-R59TVT0;'
    'DATABASE=LibraryManagementSystem1;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

def user_login(cursor):
    print("User Login")
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor.execute("SELECT * FROM Users WHERE Username = ? AND Password = ?", (username, password))
    if cursor.fetchone():
        print("Login successful.")
        user_menu(cursor)
    else:
        print("Invalid credentials. Please try again.")

def user_menu(cursor):
    while True:
        print("\nUser Menu")
        print("1. Display All Books & Availability")
        print("2. Search Books by Title")
        print("3. Search Books by Author")
        print("4. Rent a Book")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            books = display_books(cursor)
           
        elif choice == "2":
            title = input("Enter title to search: ")
            books = search_books_by_title(cursor, title)
            for book in books:
                print(book)
        elif choice == "3":
            author = input("Enter author to search: ")
            books = search_books_by_author(cursor, author)
            for book in books:
                print(book)
        elif choice == "4":
            rent_book_user(cursor)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")



def register_user(cursor):
    print("Register User")
    username = input("Enter username: ")
    password = input("Enter password: ")
    is_active = input("Is active? (0/1): ")
    cursor.execute("""
        INSERT INTO Users (Username, Password, IsActive)
        VALUES (?, ?, ?)
    """, (username, password, is_active))
    cursor.connection.commit()
    print("User registered successfully.")
