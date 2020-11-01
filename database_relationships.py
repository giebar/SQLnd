import sqlite3
from database import DatabaseContextManager

# "Foreign key table"
# Table = "Customers"
# Fields = [first_name, last_name, age, Foreign Key (compnay_id) References Companies(company_id)]
#
#
#
# Table = "Companies"
# Fields = [company_id,company_name, employee_count]
# JOIN OUTPUT: 1,John,johnathan, 30, 2 , 2 , Google, 500


# ------------------------Table Creation------------------------
def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
                 customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 first_name TEXT,
                 last_name TEXT,
                 age INTEGER,
                 company_id INTEGER,
                FOREIGN KEY (company_id) References Companies(company_id))"""
    with DatabaseContextManager("relationships") as db:
        db.execute(query)


def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS Companies(
                 company_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 company_name TEXT,
                 employee_count INTEGER)"""
    with DatabaseContextManager("relationships") as db:
        db.execute(query)


# ------------------------CRUD------------------------

# Create
def create_customer(first_name: str, last_name: str, age: int, company_id: int):
    query = """INSERT INTO Customers(first_name, last_name, age, company_id) VALUES(?,?,?,?)"""
    parameters = [first_name, last_name, age, company_id]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


def create_company(company_name: str, employee_count: int):
    query = """INSERT INTO Companies(company_name, employee_count) VALUES(?,?)"""
    parameters = [company_name, employee_count]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


# Read
def get_customers():
    query = """SELECT * FROM Customers"""
    with DatabaseContextManager("relationships") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
    print("--------------------------------------------------------")


def get_companies():
    query = """SELECT * FROM Companies"""
    with DatabaseContextManager("relationships") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
    print("--------------------------------------------------------")


# Update
def update_customer_age(age: int, customer_id: int):
    query = """UPDATE Customers
                SET age = ? 
                WHERE customer_id = ?"""
    parameters = [age, customer_id]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


def update_company_employees(employee_count: int, company_id: int):
    query = """UPDATE Companies
                SET employee_count = ? 
                WHERE company_id = ?"""
    parameters = [employee_count, company_id]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


# Delete
def delete_customer(customer_id: int):
    query = """DELETE FROM Customers
                WHERE customer_id = ?"""
    parameters = [customer_id]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


def delete_company(company_id: int):
    query = """DELETE FROM Companies
                WHERE company_id = ?"""
    parameters = [company_id]
    with DatabaseContextManager("relationships") as db:
        db.execute(query, parameters)


# Join
def join_customers_companies():
    query = """SELECT * FROM Customers
                JOIN Companies
                    ON Customers.company_id=Companies.company_id"""
    with DatabaseContextManager("relationships") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)


create_table_customers()
create_table_companies()
create_customer("Jonas", "Jonaitis", 30, 1)
create_customer("Petras", "Petraitis", 24, 3)
create_customer("Antanas", "Antanaitis", 42, 2)
create_customer("Ana", "Anaitytė", 28, 2)
create_customer("Ona", "Onaitienė", 57, 1)
create_company("Kompanija1", 2500)
create_company("Kompanija2", 3048)
create_company("Kompanija3", 125)
create_company("Kompanija4", 14)
get_customers()
get_companies()
update_customer_age(29, 4)
update_company_employees(2541, 1)
delete_customer(5)
delete_company(4)
join_customers_companies()



