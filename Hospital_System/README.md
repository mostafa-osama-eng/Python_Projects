# Hospital Queue Management System

A simple console-based hospital queue management system built with Python using clean object-oriented design and modular architecture.

This project demonstrates how to structure a small Python system into clear backend and frontend layers, similar to real-world applications.

---

## Project Structure

hospital-system/
│
├── backend/
│   ├── __init__.py
│   ├── patient.py
│   └── hospital_manager.py
│
├── frontend/
│   ├── __init__.py
│   └── frontend.py
│
├── main.py
└── README.md

---

## Features

- Add new patients with priority handling (Normal, Urgent, Super Urgent)  
- List all patients per specialization  
- Serve the next patient according to priority  
- Remove patients from a specialization  
- Clear separation of concerns:  
  - **Backend**: business logic and data models  
  - **Frontend**: user interaction and input/output  
- Fixed capacity per specialization to simulate real hospital constraints  
- Uses absolute imports and modular design  

---

## Design Overview

- **Patient**  
  Represents a single patient entity (data container) with name, priority status, and specialization.

- **HospitalManager**  
  Handles all hospital logic: adding, removing, retrieving, and ordering patients in each specialization queue according to priority.

- **Frontend**  
  Manages console-based user interaction and delegates operations to the backend.

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
