# Hospital Queue Management System

## Description
A Python-based console application for managing patient queues in a hospital.  
The system organizes patients by medical specialization and serves them according to predefined priority rules.

Supported operations:
- Adding new patients to a specialization
- Displaying all waiting patients
- Serving the next patient based on priority
- Removing patients who leave the queue

## Features
- Object-oriented design using the following classes:
  - `Patient` – represents a hospital patient
  - `HospitalManager` – contains all hospital business logic
  - `Frontend` – handles user interaction
- Priority-based queue management (Normal, Urgent, Super Urgent)
- Fixed capacity per specialization to simulate real hospital constraints
- Clear separation between business logic and input/output handling

## Installation
Clone the repository and run the main Python file using Python 3.
