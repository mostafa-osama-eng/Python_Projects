import math
def get_from_user(msg, start = 1, end = math.inf):
    """
    Safely read an integer input from the user within a given range.

    @Args:
        msg (str): Prompt message shown to the user.
        start (int): Minimum allowed value (inclusive).
        end (int): Maximum allowed value (inclusive).

    @Returns:
        int: A valid integer entered by the user.
    """
    while True:
        choice = input(msg)
        # Reject non-numeric inputs
        if not choice.isdecimal():
            print('Invalid input try again!')
        else:
            choice = int(choice)
             # Reject numbers outside the allowed range
            if choice > end or choice < start:
                print('Invalid input try again!')
                continue
        return choice

class Book:
    """
    Represents a book in the library.
    Keeps track of total copies and borrowed copies.
    """
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.total_quantity = quantity
        self.total_borrowed = 0

    def borrow(self):
        """
        Borrow one copy of the book if available.

        @Returns:
            bool: True if borrowing succeeded, False otherwise.
        """
        if self.total_quantity - self.total_borrowed == 0:
            return False
        self.total_borrowed += 1
        return True
    
    def return_copy(self):
        """
        Return one borrowed copy.
        """
        # Defensive programming: returning without borrowing is not allowed
        assert self.total_borrowed > 0
        self.total_borrowed -= 1

    def __repr__(self):
        return f'name: {self.name}, id: {self.id}, quantity: {self.total_quantity}, borrow: {self.total_borrowed}'
    
    def __str__(self):
        return f'Book name: {self.name}\t\t-id: {self.id} - total quantity: {self.total_quantity} - total borrowed: {self.total_borrowed}'

class User:
    """
    Represents a library user and the books they borrowed.
    """
    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.borrowed_books = []

    def borrow(self, book):
        """
        Register a borrowed book for the user.
        """
        self.borrowed_books.append(book) 
    
    def is_borrowed(self, book):
        """
        Check whether the user has already borrowed a specific book.
        """
        for b in self.borrowed_books:
            if book == b:
                return True
        return False

    def return_copy(self, book):
        """
        Remove a borrowed book from the user's list.
        """
        for idx, b in enumerate(self.borrowed_books):
            if book == b:
                del self.borrowed_books[idx]
                break

    def simple_str(self):
        """
        Human-readable representation of the user and borrowed books.
        """
        ret = f'User name: {self.name}\t\t-id: {self.id}'
        ret += f'\n\tBorrowed books:\n'
        for book in self.borrowed_books:
            ret += f'\t{book}\n'
        return ret
    
    def __repr__(self):
        return f'name: {self.name}, id: {self.id}'
    
    def __str__(self):
        return self.simple_str()

class Manager:
    """
    Core system logic.
    Manages books, users, borrowing, and returning.
    """
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, id, name, quantity):
        """
        Add a new book to the library.
        """
        self.books.append(Book(id, name, quantity))

    def print_books(self):
        """
        Return a list of all books.
        """
        # there's no books available
        if len(self.books) == 0 :
            return False
        # Return a copy to protect internal state
        return [book for book in self.books]
    
    def add_user(self, name, id):
        """
        Add a new user to the system.
        """
        self.users.append(User(name, id))

    def print_users(self):
        """
        Return a list of all users.
        """
        # there's no users available
        if len(self.users) == 0 :
            return False
        return [user for user in self.users]    # for security reason

    def print_books_by_prefix(self, pref):
        """
        Search books by name prefix.
        """
        books = [book for book in self.books if book.name[: len(pref)] == pref]  # manually check, i can use startswith()
        # ther's no books with this prefix
        if len(books) == 0:
            return False
        return books

    def check_user(self, user_name):
        """
        Find and return a user by name.
        """
        for user in self.users:
            if user.name == user_name:
                return user
        return False
            
    def check_book(self, book_name):
        """
        Find and return a book by name.
        """
        for book in self.books:
            if book.name == book_name:
                return book
        return False

    def borrow_book(self, user_name, book_name):
        """
        Borrow a book for a user if possible.
        """
        if (user := self.check_user(user_name)) and (book := self.check_book(book_name)):
            if book.borrow():
                user.borrow(book)
                return True
        return False

    def return_book(self, user_name, book_name):
        """
        Return a borrowed book.
        """
        if (user := self.check_user(user_name)) and (book := self.check_book(book_name)):
                if user.is_borrowed(book):
                    user.return_copy(book)
                    book.return_copy()
                    return True
        return False

    def users_borrowed(self, book_name):
        """
        Get all users who borrowed a specific book.
        """
        if book := self.check_book(book_name):
            return [user for user in self.users if user.is_borrowed(book)]
        return False

class Frontend:
    """
    Console-based user interface.
    Handles input/output and delegates logic to Manager.
    """
    def __init__(self):
        self.admin = Manager()

    def print_menu(self):
        """
        Display the main menu.
        """
        print('Program options:')
        choices = ['Add book', 'Print library books', 'Print books by prefix', 'Add user',
                   'Borrow book', 'Return book', 'Print users borrowed book', 'Print users', 'End the program']
        choices = [f'\t{idx + 1}) {sen}' for idx, sen in enumerate(choices)]
        self.num_choices = len(choices)
        print('\n'.join(choices))

    def run(self):
        """
        Main application loop.
        """
        while True:
            # print main menu and get the choice from the user
            self.print_menu()
            choice = get_from_user('Enter your choice: ', 1, self.num_choices)

            # add new book
            if choice == 1:
                # get book's data
                id = get_from_user('Enter book id: ')
                name = input('Enter book name: ')
                quantity = get_from_user('How many copies: ')
                # add
                self.admin.add_book(id, name, quantity)

            # print all books
            elif choice == 2:
                # there's a book available
                if books := self.admin.print_books():
                    for book in books:
                        print(book)
                # no books exist
                else:
                    print('No books yet!')
            
            # print books by prefix
            elif choice == 3:
                pref = input('Enter book name prefix: ')
                if books := self.admin.print_books_by_prefix(pref):
                    for book in books:
                        print(book)
                else:
                    print('No such books with this prefix')

            # add user
            elif choice == 4:
                # read user's data
                name = input('Enter user name: ')
                id = get_from_user('Enter user id: ')
                # add
                self.admin.add_user(name, id)
            
            # borrow a book
            elif choice == 5:
                print('Enter user name and book name:')
                user_name = input('Enter user name: ')
                book_name = input('Enter book name: ')

                if self.admin.borrow_book(user_name, book_name):
                    print(f'{user_name} borrowed {book_name} successfully')
                else:
                    print(f"{user_name} can't borrow {book_name}")

            # return a book
            elif choice == 6:
                print('Enter user name and book name:')
                user_name = input('Enter user name: ')
                book_name = input('Enter book name: ')

                if self.admin.return_book(user_name, book_name):
                    print(f'{user_name} returned {book_name}')
                else:
                    print(f"{user_name} didn't borrow {book_name}")

            # print users borrowed books
            elif choice == 7:
                book_name = input('Enter book name: ')
                if users := self.admin.users_borrowed(book_name):
                    print('Users borrowed this book: ')
                    for user in users:
                        print(user)
                else:
                    print('Invalid!')

            # print all users
            elif choice == 8:
                # there's a user available
                if users := self.admin.print_users():
                    for user in users:
                        print(user)
                # no users exist
                else:
                    print('No users yet!')
            # exit the program
            elif choice == 9:
                print('Good bye')
                break

def add_dummy_data(app):
    """
    Populate the system with sample data for testing.
    add 10 books and 5 users.
    """
    # add books
    for i in range(10):
        app.admin.add_book(i + i * 2, f'book{i + 1}', i)
    # add users
    for i in range(5):
        app.admin.add_user(f'user{i + 1}', i ** 5 + 10)

if __name__ == '__main__':
    app = Frontend()
    # add_dummy_data(app)     
    app.run()

    