from employee_service import (
    add_employee,
    read_employees,
    update_salary,
    get_employee_by_id,
    delete_employee,
)


def menu() -> None:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Get Employee By ID")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")


def main() -> None:
    while True:
        menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            salary = int(input("Enter salary: "))
            add_employee(name, email, salary)

        elif choice == 2:
            read_employees()

        elif choice == 3:
            emp_id = int(input("Enter employee ID: "))
            get_employee_by_id(emp_id)

        elif choice == 4:
            emp_id = int(input("Enter employee ID: "))
            salary = int(input("Enter new salary: "))
            update_salary(emp_id, salary)

        elif choice == 5:
            emp_id = int(input("Enter employee ID: "))
            delete_employee(emp_id)

        elif choice == 6:
            print("Exiting system... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()