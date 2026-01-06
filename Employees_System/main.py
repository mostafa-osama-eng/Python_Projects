"""
Employee System
Author: Mostafa Osama
Date: 2025-12-17
Description:
    A simple Python program to manage employees with OOP.
    Features: Add, list, delete by age, update salary.
"""
# imports
from frontend.frontdend import Frontend

def main():
    # Initialize Frontend and start main loop
    app = Frontend()
    app.run()
    
if __name__ == '__main__':
    main()