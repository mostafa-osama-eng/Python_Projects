"""
Hospital Queue Management System
Author: Mostafa Osama
Date: 2025-12-18
Description:
    A Python console application to manage hospital patient queues using OOP.
    Features:
    - Add new patients with priority handling (Normal, Urgent, Super Urgent)
    - List all patients per specialization
    - Serve the next patient according to priority
    - Remove patients from a specialization
"""
from frontend.frontend import Frontend

if __name__ == '__main__':
    app = Frontend()
    app.run()
