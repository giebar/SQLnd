import sqlite3
from database import DatabaseContextManager


# Tables = "Customer"
# fields = [first_name, last_name, address, age]

def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             first_name TEXT,
             last_name TEXT,
             address TEXT,
             age INTEGER)"""
    with DatabaseContextManager("CRUD") as db:
        db.execute(query)


# Create function
def create_customer(first_name: str, last_name: str, address: str, age: int):
    query = """INSERT INTO Customers(first_name, last_name, address, age) VALUES(?,?,?,?)"""
    # Question marks are used in initial query to have placeholders for upcoming parameters.
    # (This is used to protect ourselves from SQL Injection attacks)
    parameters = [first_name, last_name, address, age]
    # Parameters are used to pass values that were given when calling the function.
    with DatabaseContextManager("CRUD") as db:
        db.execute(query, parameters)


# Read function
def get_customer():
    query = """SELECT * FROM Customers"""
    with DatabaseContextManager("CRUD") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


# Update function
def update_customer(age: int, first_name: str, last_name: str):
    query = """UPDATE Customers
                SET age = ?
                WHERE first_name = ? AND last_name = ?"""
    parameters = [age, first_name, last_name]
    with DatabaseContextManager("CRUD") as db:
        db.execute(query, parameters)


# Delete function
def delete_customer(last_name: str):
    query = """DELETE FROM Customers
                WHERE last_name = ?"""
    parameters = [last_name]
    with DatabaseContextManager("CRUD") as db:
        db.execute(query, parameters)


create_table_customers()
create_customer('John', 'Johnson', 'Kaunas', 25)
update_customer(26, 'John', 'Johnson')
delete_customer('Johnson')
get_customer()

