import pyodbc
import datetime



def add_books(cursor):
    print("Add Books to Database")
    title = input("Enter title: ")
    author = input("Enter author: ")

    is_available = input("Is available? (0/1): ")
    cursor.execute("""
        INSERT INTO Books (Title, Author, IsAvailable)
        VALUES (?, ?, ?)
    """, (title, author, is_available))
    cursor.connection.commit()
    print("Book added successfully.")

def display_books(cursor):
    print("Display Books")
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    for book in books:
        print(book)