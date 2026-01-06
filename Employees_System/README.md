# Employee Management System

A simple console-based employee management system built with Python using clean object-oriented design and modular architecture.

This project demonstrates how to structure a small Python system into clear backend and frontend layers, similar to real-world applications.

---

## Project Structure

employee-system/
│
├── backend/
│   ├── __init__.py
│   ├── employee.py
│   └── employee_manager.py
│
├── frontend/
│   ├── __init__.py
│   └── frontend.py
│
├── main.py
└── README.md

---

## Features

- Add new employees  
- List all employees  
- Delete employees by age range  
- Update employee salary by name  
- Clear separation of concerns:  
  - **Backend**: business logic and data models  
  - **Frontend**: user interaction and input/output  
- Uses absolute imports and modular design  

---

## Design Overview

- **Employee**  
  Represents a single employee entity (data container).

- **EmployeeManager**  
  Handles all business logic: adding, deleting, updating, and retrieving employees.

- **Frontend**  
  Manages user interaction and delegates operations to the backend.

- **main.py**  
  Application entry point that wires all components together.

This design follows basic software engineering principles:  
- Single Responsibility  
- Separation of concerns  
- Loose coupling between components  

---

## How to Run

Make sure you run the program **from the project root directory**:

```bash
python main.py
