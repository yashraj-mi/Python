# Expense Tracker CLI

A Splitwise-style Expense Tracker built using Python, SQLAlchemy ORM, PostgreSQL, and Argparse.

The application allows users to manage shared expenses, settlements, balances, and reports entirely from the command line.

---

## Features

### User Management

* Add User
* Get User by ID
* List Users
* Update User
* Delete User

### Expense Management

* Add Expense
* Get Expense Details
* List All Expenses
* Update Expense
* Delete Expense

### Settlement Management

* Automatic Settlement Creation
* Mark Settlement as Paid
* View Pending Settlements
* View Paid Settlements
* View All Settlements

### Balance Tracking

* Total Amount Owed
* Total Amount Receivable
* Net Balance Calculation

### Reports

* User Expense Report
* Monthly Expense Report
* Category-wise Expense Report
* Expenses Paid By User
* Group Expense Summary

---

## Tech Stack

* Python 3.10+
* SQLAlchemy ORM
* PostgreSQL
* Argparse
* python-dotenv

---

## Project Structure

```text
expense_tracker/

├── main.py
├── README.md
├── requirements.txt
├── pyproject.toml
├── .env.example

├── cli/
│   ├── parser.py
│   ├── command_config.py
│   └── commands/

├── database/
│   ├── db.py
│   ├── decorators.py
│   └── create_tables.py

├── models/
│   ├── user.py
│   ├── expense.py
│   ├── participant.py
│   └── settlement.py

├── services/
│   ├── user_service.py
│   ├── expense_service.py
│   ├── settlement_service.py
│   ├── balance_service.py
│   ├── report_service.py
│   └── summary_service.py

└── schemas/
    └── helper.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<username>/expense_tracker.git

cd expense_tracker
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Linux / Mac

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
DB_URL=postgresql://username:password@localhost:5432/expense_tracker
```

Example:

```env
DB_URL=postgresql://postgres:postgres@localhost:5432/expense_tracker
```

---

## Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE expense_tracker;
```

Create tables:

```bash
python database/create_tables.py
```

---

## Running the Application

### Using Python

```bash
python main.py -h
```

### Using Installed CLI Command

```bash
expense-tracker -h
```

---

## User Commands

### Add User

```bash
expense-tracker add-user --name Yashraj
```

### Get User

```bash
expense-tracker get-user --user-id 1
```

### List Users

```bash
expense-tracker list-users
```

### Update User

```bash
expense-tracker update-user --user-id 1 --name Yash
```

### Delete User

```bash
expense-tracker delete-user --user-id 1
```

---

## Expense Commands

### Add Expense

```bash
expense-tracker add-expense \
--description Lunch \
--category Food \
--amount 3000 \
--paid-by 1 \
--participants 1 2 3
```

### Get Expense

```bash
expense-tracker get-expense --expense-id 1
```

### List Expenses

```bash
expense-tracker get-all-expenses
```

### Delete Expense

```bash
expense-tracker delete-expense --expense-id 1
```

---

## Settlement Commands

### Mark Settlement Paid

```bash
expense-tracker mark-paid --settlement-id 1
```

### Get Pending Settlements

```bash
expense-tracker get-pending-settlements --user-id 1
```

### Get Paid Settlements

```bash
expense-tracker get-paid-settlements --user-id 1
```

### Get All Settlements

```bash
expense-tracker get-all-settlements
```

---

## Balance Commands

### Get Total Owed

```bash
expense-tracker get-total-owed --user-id 1
```

### Get Total Receivable

```bash
expense-tracker get-total-receivable --user-id 1
```

### Get Net Balance

```bash
expense-tracker get-net-balance --user-id 1
```

---

## Report Commands

### User Expense Report

```bash
expense-tracker get-user-expenses --user-id 1
```

### Monthly Expense Report

```bash
expense-tracker get-monthly-expenses --month 6
```

### Category Report

```bash
expense-tracker get-category-report
```

### Expenses Paid By User

```bash
expense-tracker get-expenses-paid-by-user --user-id 1
```

### Group Summary

```bash
expense-tracker get-group-summary --expense-id 1
```

---

## Example Workflow

### 1. Create Users

```bash
expense-tracker add-user --name Yashraj
expense-tracker add-user --name Romit
expense-tracker add-user --name Sahdev
```

### 2. Add Expense

```bash
expense-tracker add-expense \
--description Hotel \
--category Travel \
--amount 9000 \
--paid-by 1 \
--participants 1 2 3
```

### 3. Check Balances

```bash
expense-tracker get-total-receivable --user-id 1
expense-tracker get-total-owed --user-id 2
expense-tracker get-total-owed --user-id 3
```

### 4. Mark Settlement Paid

```bash
expense-tracker mark-paid --settlement-id 1
```

---

## Architecture

```text
CLI Layer
    ↓
Service Layer
    ↓
SQLAlchemy ORM
    ↓
PostgreSQL Database
```

### Responsibilities

* CLI Layer handles user input.
* Service Layer contains business logic.
* Models represent database tables.
* Database Layer manages sessions and transactions.

```



