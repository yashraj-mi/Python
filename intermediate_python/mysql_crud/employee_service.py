from db import get_connection
from db_helper import db_cursor


def add_employee(name: str, email: str, salary: int) -> None:
    """

    Add Employee in employees table
    with their Name, Email, and Salary.

    """

    query = """
        INSERT INTO employees (name, email, salary)
        VALUES (%s, %s, %s)
    """

    with db_cursor() as cursor:
        cursor.execute(query, (name, email, salary))

    print("Employee added successfully")


def read_employees() -> None:
    """Fetch all Employees from employees table."""

    query = "SELECT * FROM employees"

    with db_cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    for row in rows:
        print(row)


def get_employee_by_id(emp_id: int) -> None:
    """Search employee from employees table by their Id."""

    query = "SELECT * FROM employees WHERE id = %s"

    with db_cursor() as cursor:
        cursor.execute(query, (emp_id,))
        employee = cursor.fetchone()

    print(employee)


def update_salary(emp_id: int, salary: int) -> None:
    """Update employee's salary."""

    query = "UPDATE employees SET salary = %s WHERE id = %s"

    with db_cursor() as cursor:
        cursor.execute(query, (salary, emp_id))

    print("Salary updated successfully")


def delete_employee(emp_id: int) -> None:
    """Delete employee from employees table by their Id."""

    query = "DELETE FROM employees WHERE id = %s"

    with db_cursor() as cursor:
        cursor.execute(query, (emp_id,))

    print("Employee deleted successfully")
