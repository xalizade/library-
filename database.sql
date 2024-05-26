CREATE DATABASE LibraryManagementSystem1;

USE LibraryManagementSystem;

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

CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY IDENTITY,
    Name NVARCHAR(255),
    Bio NVARCHAR(MAX)
);

CREATE TABLE Loans (
    LoanID INT IDENTITY(1,1) PRIMARY ,
    BookID INT,
    UserID INT,
    LoanDate DATETIME,
    IsReturned BIT,
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

INSERT INTO Books (Title, Author, IsAvailable) VALUES ('1984', 'George Orwell', 1);
INSERT INTO Books (Title, Author, IsAvailable) VALUES ('Pride and Prejudice', 'Jane Austen', 1);
INSERT INTO Books (Title, Author, IsAvailable) VALUES ('White Fang', 'Jack London', 1);
INSERT INTO Books (Title, Author, IsAvailable) VALUES ('Gnosis', 'Adam Fawer', 1);
INSERT INTO Books (Title, Author, IsAvailable) VALUES ('Silahlara veda', 'Ernest Hemingway', 1);
INSERT INTO Books (Title, Author, IsAvailable) VALUES ('Serenad', 'Zülfi Livaneli', 1);
INSERT INTO Books (Title, Author, IsAvailable) VALUES ('Kumru ile Kumru', 'Tahsin Yücel', 1);
INSERT INTO Books (Title, Author, IsAvailable) VALUES ('Dune', 'Frank Herbert', 1);
