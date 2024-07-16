from datetime import datetime

class Book:
    def __init__(self, book_name, author, book_id, rental_date, due_date):
        self.book_name = book_name
        self.author = author
        self.book_id = book_id
        self.rental_date = rental_date
        self.due_date = due_date

class Customer:
    def __init__(self, customer_id, name, address, contact_no):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.contact_no = contact_no
        self.books = []
        self.penalty_amount = 0.0

    def add_book(self, book):
        self.books.append(book)

    def edit_book(self, book_id, new_book):
        for i, book in enumerate(self.books):
            if book.book_id == book_id:
                self.books[i] = new_book
                return True
        return False

    def calculate_penalty(self, current_date):
        self.penalty_amount = 0.0
        for book in self.books:
            overdue_days = (current_date - datetime.strptime(book.due_date, "%d/%m/%Y")).days
            if overdue_days > 5:
                if 5 < overdue_days <= 7:
                    self.penalty_amount += (overdue_days - 5) * 2
                elif 7 < overdue_days <= 14:
                    self.penalty_amount += (7 - 5) * 2 + (overdue_days - 7) * 3.5
                elif 14 < overdue_days <= 30:
                    self.penalty_amount += (7 - 5) * 2 + (14 - 7) * 3.5 + (overdue_days - 14) * 4
                elif overdue_days > 30:
                    self.penalty_amount += (7 - 5) * 2 + (14 - 7) * 3.5 + (30 - 14) * 4 + (overdue_days - 30) * 5

    def is_overdue(self, current_date):
        for book in self.books:
            if datetime.strptime(book.due_date, "%d/%m/%Y") < current_date:
                return True
        return False

class LibrarySystem:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def edit_customer(self, customer_id, new_customer):
        for i, customer in enumerate(self.customers):
            if customer.customer_id == customer_id:
                self.customers[i] = new_customer
                return True
        return False

    def list_customers(self):
        for customer in self.customers:
            customer.calculate_penalty(datetime.now())
            print(f"ID: {customer.customer_id} | Name: {customer.name} | Address: {customer.address} | Contact No: {customer.contact_no} | Penalty Amount: RM {customer.penalty_amount}")
            for book in customer.books:
                print(f"  Book Name: {book.book_name} | Author: {book.author} | Rental Date: {book.rental_date} | Due Date: {book.due_date}")

    def list_overdue_customers(self):
        current_date = datetime.now()
        for customer in self.customers:
            if customer.is_overdue(current_date):
                customer.calculate_penalty(datetime.now())
                print(f"! Overdue ! ID: {customer.customer_id} | Name: {customer.name} | Address: {customer.address} | Contact No: {customer.contact_no} | Penalty Amount: RM {customer.penalty_amount}")
                for book in customer.books:
                    if datetime.strptime(book.due_date, "%d/%m/%Y") < current_date:
                        print(f"  ! Overdue ! Book Name: {book.book_name} | Author: {book.author} | Rental Date: {book.rental_date} | Due Date: {book.due_date}")

def main():
    library = LibrarySystem()

    while True:
        print("\nLibrary System Menu:")
        print("1. Add new customer")
        print("2. Edit existing customer")
        print("3. List all customers")
        print("4. List overdue customers")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            customer_id = int(input("Enter Customer ID: "))
            name = input("Enter Customer Name: ")
            address = input("Enter Customer Address: ")
            contact_no = input("Enter Customer Contact No: ")
            customer = Customer(customer_id, name, address, contact_no)

            while True:
                add_book = input("Do you want to add a book for this customer? (yes/no): ")
                if add_book.lower() == 'yes':
                    book_name = input("Enter Book Name: ")
                    author = input("Enter Author: ")
                    book_id = int(input("Enter Book ID: "))
                    rental_date = input("Enter Rental Date (dd/mm/yyyy): ")
                    due_date = input("Enter Due Date (dd/mm/yyyy): ")
                    book = Book(book_name, author, book_id, rental_date, due_date)
                    customer.add_book(book)
                else:
                    break
            library.add_customer(customer)

        elif choice == '2':
            customer_id = int(input("Enter Customer ID to edit: "))
            name = input("Enter New Customer Name: ")
            address = input("Enter New Customer Address: ")
            contact_no = input("Enter New Customer Contact No: ")
            new_customer = Customer(customer_id, name, address, contact_no)

            while True:
                add_book = input("Do you want to add/edit a book for this customer? (yes/no): ")
                if add_book.lower() == 'yes':
                    book_name = input("Enter Book Name: ")
                    author = input("Enter Author: ")
                    book_id = int(input("Enter Book ID: "))
                    rental_date = input("Enter Rental Date (dd/mm/yyyy): ")
                    due_date = input("Enter Due Date (dd/mm/yyyy): ")
                    book = Book(book_name, author, book_id, rental_date, due_date)
                    new_customer.add_book(book)
                else:
                    break
            library.edit_customer(customer_id, new_customer)

        elif choice == '3':
            library.list_customers()

        elif choice == '4':
            library.list_overdue_customers()

        elif choice == '5':
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()