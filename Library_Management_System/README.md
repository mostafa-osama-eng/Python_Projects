# 📚 Library Management System (Python – Console Application)

A simple console-based **Library Management System** implemented in Python using **Object-Oriented Programming (OOP)** principles.  
The system is designed for an **admin user** to manage books, users, and borrowing operations.

This project focuses on **clean architecture, separation of concerns, and practical OOP usage**

---

## 🚀 Features

### 📖 Book Management
- Add new books with:
  - Book ID
  - Book name
  - Total quantity
- List all books in the library
- Search books by **name prefix**
- Track how many copies are currently borrowed

### 👤 User Management
- Add new users with:
  - User ID
  - User name
- List all registered users

### 🔄 Borrow & Return Operations
- Borrow a book (only if copies are available)
- Return a borrowed book
- Prevent invalid borrow/return actions
- View all users who borrowed a specific book

---

## 🧠 System Design Overview

The system is structured using clear responsibilities:

### `Book`
- Represents a single book in the library
- Tracks:
  - Total quantity
  - Number of borrowed copies
- Handles borrow and return logic

### `User`
- Represents a library user
- Tracks borrowed books
- Ensures users can only return books they borrowed

### `Manager`
- Core business logic layer
- Manages:
  - Books
  - Users
  - Borrowing & returning rules
- Acts as the system controller

### `Frontend`
- Console-based interface
- Handles:
  - Menu display
  - User input
  - Output formatting
- Delegates logic to `Manager`

---

## 🛠 Technologies Used

- **Python 3**
- Object-Oriented Programming (OOP)
- Console I/O

No external libraries are required.

---
