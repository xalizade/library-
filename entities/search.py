# entities/search.py

import pyodbc
def search_books_by_title(cursor, title):
    cursor.execute("SELECT * FROM Books WHERE Title LIKE ?", ('%' + title + '%',))
    return cursor.fetchall()

def search_books_by_author(cursor, author):
    cursor.execute("SELECT * FROM Books WHERE Author LIKE ?", ('%' + author + '%',))
    return cursor.fetchall()
