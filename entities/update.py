# entities/update.py

import pyodbc
import datetime

def update_rent_details(cursor):
    print("Update Rent Details")
    loan_id = input("Enter Loan ID: ")
    is_returned = input("Is returned? (0/1): ")
    
    # Update the Loans table
    cursor.execute("UPDATE Loans SET IsReturned = ? WHERE LoanID = ?", (is_returned, loan_id))
    
    # Retrieve the BookID from the Loans table
    cursor.execute("SELECT BookID FROM Loans WHERE LoanID = ?", (loan_id,))
    book_id = cursor.fetchone()[0]
    
    # Update the Books table based on the return status
    if is_returned == '1':
        cursor.execute("UPDATE Books SET IsAvailable = 1 WHERE BookID = ?", (book_id,))
    else:
        cursor.execute("UPDATE Books SET IsAvailable = 0 WHERE BookID = ?", (book_id,))
    
    cursor.connection.commit()
    print("Rent details and book availability updated successfully.")



def rent_book_user(cursor):
    book_id = input("Enter the ID of the book to rent: ")
    user_id = input("Enter your user ID: ")
    cursor.execute("SELECT IsAvailable FROM Books WHERE BookID = ?", (book_id,))
    is_available = cursor.fetchone()
    
    if is_available and is_available[0]:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        cursor.execute("""
            INSERT INTO Loans (BookID, UserID, LoanDate, IsReturned)
            VALUES (?, ?, ?, ?)
        """, (book_id, user_id, current_date, 0))
        
        cursor.execute("UPDATE Books SET IsAvailable = 0 WHERE BookID = ?", (book_id,))
        cursor.connection.commit()
        
        print("Book rented successfully.")
    else:
        print("Book is not available.")
