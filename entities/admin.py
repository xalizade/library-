# entities/admin.py
import pyodbc
from entities.book import display_books, add_books
from entities.delete import delete_books,delete_users
from entities.update import update_rent_details
from entities.search import search_books_by_title,search_books_by_author
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-R59TVT0;'
    'DATABASE=LibraryManagementSystem1;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

def admin_login(cursor):
    print("Admin Login")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    cursor.execute("SELECT * FROM Admins WHERE Username = ? AND Password = ?", (username, password))
    if cursor.fetchone():
        print("Login successful.")
        admin_menu(cursor)
    else:
        print("Invalid credentials. Please try again.")


def admin_menu(cursor):
    while True:
        print("\nAdmin Menu")
        print("1. Add Books to Database")
        print("2. Display Books")
        print("3. Search Books by Title")
        print("4. Search Books by Author")
        print("5. Delete Books")
        print("6. Display Users")
        print("7. Add Users")
        print("8. Delete Users")
        print("9. Update Rent Details")
        print("10. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_books(cursor)
        elif choice == "2":
            display_books(cursor)
        elif choice == "3":
            title = input("Enter title to search: ")
            books = search_books_by_title(cursor, title)
            for book in books:
                print(book)
        elif choice == "4":
            author = input("Enter author to search: ")
            books = search_books_by_author(cursor, author)
            for book in books:
                print(book)
        elif choice == "5":
            delete_books(cursor)
        elif choice == "6":
            display_users(cursor)
        elif choice == "7":
            add_users(cursor)
        elif choice == "8":
            delete_users(cursor)
        elif choice == "9":
            update_rent_details(cursor)
        elif choice == "10":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")



def display_users(cursor):
    print("Display Users")
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    for user in users:
        print(user)

def add_users(cursor):
    print("Add Users")
    username = input("Enter username: ")
    password = input("Enter password: ")
    is_active = input("Is active? (0/1): ")
    cursor.execute("""
        INSERT INTO Users (Username, Password, IsActive)
        VALUES (?, ?, ?)
    """, (username, password, is_active))
    cursor.connection.commit()
    print("User added successfully.")

