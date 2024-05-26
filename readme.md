# Library Management System

This project is a Library Management System implemented in Python using pyodbc for database operations. It includes functionalities for both admin and user roles.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Admin Functions](#admin-functions)
- [User Functions](#user-functions)
- [Database Setup](#database-setup)
- [Contributing](#contributing)
- [License](#license)

## Features

- Admin and user login
- User registration
- Admin functionalities: add, display, delete books and users, update rent details
- User functionalities: display all books, search books by title or author, rent books

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/LibraryManagementSystem.git
    cd LibraryManagementSystem
    ```

2. Install the required Python packages:

    ```sh
    pip install pyodbc
    ```

3. Ensure you have SQL Server installed and running.

## Usage

1. Update the database connection details in `app.py`:

    ```python
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=your_server_name;'
        'DATABASE=LibraryManagementSystem;'
        'Trusted_Connection=yes;'
    )
    ```

2. Run the application:

    ```sh
    python app.py
    ```

## Admin Functions

- **Login**: Admins can log in using their credentials.
- **Add Books**: Add new books to the database.
- **Display Books**: View all books in the database.
- **Delete Books**: Remove books from the database.
- **Display Users**: View all registered users.
- **Add Users**: Register new users.
- **Delete Users**: Remove users from the database.
- **Update Rent Details**: Update the rental status of books.
- **Logout**: Admins can log out.

## User Functions

- **Login**: Users can log in using their credentials.
- **Register**: Register as a new user.
- **Display All Books**: View all books and their availability.
- **Search Books by Title**: Search for books by title.
- **Search Books by Author**: Search for books by author.
- **Rent a Book**: Rent a book if available.
- **Logout**: Users can log out.

## Database Setup

1. Create the `LibraryManagementSystem` database in your SQL Server.
2. Run the following SQL script to create the necessary tables:

    ```sql
    CREATE TABLE Users (
        UserID INT PRIMARY KEY IDENTITY,
        Username NVARCHAR(255),
        Password NVARCHAR(255),
        IsActive BIT
    );

    CREATE TABLE Books (
        BookID INT PRIMARY KEY IDENTITY,
        Title NVARCHAR(255),
        Author NVARCHAR(255),
        IsAvailable BIT
    );

    CREATE TABLE Loans (
        LoanID INT PRIMARY KEY IDENTITY,
        BookID INT,
        UserID INT,
        LoanDate DATETIME,
        IsReturned BIT,
        FOREIGN KEY (BookID) REFERENCES Books(BookID),
        FOREIGN KEY (UserID) REFERENCES Users(UserID)
    );
    ```

3. Insert initial data into the tables (optional):

    ```sql
    -- Insert admin user
    INSERT INTO Users (Username, Password, IsActive) VALUES ('admin', 'admin_password', 1);

    -- Insert sample books
    INSERT INTO Books (Title, Author, IsAvailable) VALUES ('White Fang', 'Jack London', 1);
    INSERT INTO Books (Title, Author, IsAvailable) VALUES ('Gnosis', 'Adam Fawer', 1);
    INSERT INTO Books (Title, Author, IsAvailable) VALUES ('Silahlara Veda', 'Ernest Hemingway', 1);
    INSERT INTO Books (Title, Author, IsAvailable) VALUES ('Serenad', 'Zülfü Livaneli', 1);
    INSERT INTO Books (Title, Author, IsAvailable) VALUES ('Kumru ile Kumru', 'Tahsin Yücel', 1);
    INSERT INTO Books (Title, Author, IsAvailable) VALUES ('Dune', 'Frank Herbert', 1);
    ```