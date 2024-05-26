# entities/delete.py

import pyodbc

def delete_books(cursor):
    print("Delete Books")
    book_id = input("Enter the ID of the book to delete: ")
    cursor.execute("DELETE FROM Books WHERE BookID = ?", (book_id,))
    cursor.connection.commit()
    print("Book deleted successfully.")

def delete_users(cursor):
    print("Delete Users")
    user_id = input("Enter the ID of the user to delete: ")
    cursor.execute("DELETE FROM Users WHERE UserID = ?", (user_id,))
    cursor.connection.commit()
    print("User deleted successfully.")
