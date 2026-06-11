# Expense Tracker CLI

A Splitwise-style Expense Tracker built with Python, SQLAlchemy ORM, PostgreSQL, and Argparse.

This project allows users to:

* Create and manage users
* Record shared expenses
* Split expenses among participants
* Track settlements
* Calculate balances
* Generate reports and summaries
* Manage everything through a command-line interface

---

# Features

## User Management

* Add user
* Get user by ID
* List all users
* Update user
* Delete user

## Expense Management

* Add expense
* Get expense details
* List all expenses
* Update expense
* Delete expense

## Settlement Management

* Create settlements automatically
* Mark settlement as paid
* View pending settlements
* View paid settlements
* View all settlements

## Balance Tracking

* Total amount owed by a user
* Total amount receivable by a user
* Net balance calculation

## Reports

* User expense report
* Monthly expense report
* Category-wise expense report
* Expenses paid by a specific user
* Expense participant summary

---

# Tech Stack

* Python 3.10+
* SQLAlchemy ORM
* PostgreSQL
* Argparse

---

# Project Structure

expense_tracker/

├── main.py

├── requirements.txt

├── README.md

│

├── cli/

│   ├── parser.py

│   ├── command_config.py

│   └── commands/

│

├── database/

│   ├── db.py

│   ├── decorators.py

│   └── create_tables.py

│

├── models/

│   ├── user.py

│   ├── expense.py

│   ├── participant.py

│   └── settlement.py

│

├── services/

│   ├── user_service.py

│   ├── expense_service.py

│   ├── settlement_service.py

│   ├── balance_service.py

│   ├── report_service.py

│   └── summary_service.py

│

├── schemas/

│   └── helper.py

│


---

# Installation

Clone the repository:

git clone <repository-url>

cd expense_tracker

Create virtual environment:

python -m venv .venv

Activate environment:

Linux/Mac:

source .venv/bin/activate

Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

---

# Database Configuration

Update DATABASE_URL inside:

database/db.py

Example:

DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5432/expense_tracker"

Create tables:

python main.py create-tables

or

python database/create_tables.py

---

# Available Commands

## User Commands

Add User

python main.py add-user --name Yashraj

Get User

python main.py get-user --user-id 1

List Users

python main.py list-users

Update User

python main.py update-user --user-id 1 --name Yash

Delete User

python main.py delete-user --user-id 1

---

## Expense Commands

Add Expense

python main.py add-expense 
--description Lunch 
--category Food 
--amount 3000 
--paid-by 1 
--participants 1 2 3

Get Expense

python main.py get-expense --expense-id 1

List Expenses

python main.py get-all-expenses

Delete Expense

python main.py delete-expense --expense-id 1

---

## Settlement Commands

Mark Settlement Paid

python main.py mark-paid --settlement-id 1

Get Pending Settlements

python main.py get-pending-settlements --user-id 1

Get Paid Settlements

python main.py get-paid-settlements --user-id 1

Get All Settlements

python main.py get-all-settlements

---

## Balance Commands

Get Total Owed

python main.py get-total-owed --user-id 1

Get Total Receivable

python main.py get-total-receivable --user-id 1

Get Net Balance

python main.py get-net-balance --user-id 1

---

## Report Commands

User Expense Report

python main.py get-user-expenses --user-id 1

Monthly Expense Report

python main.py get-monthly-expenses --month 6

Category Report

python main.py get-category-report

Expenses Paid By User

python main.py get-expenses-paid-by-user --user-id 1

Group Summary

python main.py get-group-summary --expense-id 1

---

# Example Workflow

Step 1: Create users

python main.py add-user --name Yashraj

python main.py add-user --name Romit

python main.py add-user --name Sahdev

Step 2: Add expense

python main.py add-expense 
--description Hotel 
--category Travel 
--amount 9000 
--paid-by 1 
--participants 1 2 3

Step 3: Check balances

python main.py get-total-receivable --user-id 1

python main.py get-total-owed --user-id 2

python main.py get-total-owed --user-id 3

Step 4: Mark settlement paid

python main.py mark-paid --settlement-id 1

---

# Architecture

The application follows a layered architecture:

CLI Layer
↓
Service Layer
↓
SQLAlchemy ORM
↓
PostgreSQL Database

Responsibilities:

* CLI handles user input.
* Services contain business logic.
* Models represent database tables.
* Database layer manages sessions and transactions.

---

# Future Improvements

* Alembic migrations
* Unit tests
* Docker support
* REST API using FastAPI
* JWT authentication
* Group-based expenses
* Unequal expense splitting
* Export reports to CSV/PDF
* Web dashboard

---

# Learning Outcomes

This project demonstrates:

* Python project structure
* SQLAlchemy ORM
* PostgreSQL integration
* Relationships and Foreign Keys
* One-to-Many relationships
* Session management
* Decorators
* Argparse CLI development
* Service-oriented architecture
* Error handling and validation
* Report generation
* Business logic implementation

---

Made for learning backend architecture and ORM design using Python.
