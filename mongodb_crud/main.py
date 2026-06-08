from student_service import (
    add_student,
    get_students,
    update_student,
    delete_student,
    delete_all_students,
    get_student_by_name
)

def display_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Get Student by Name")
    print("6. Delete All Students")
    print("7. Exit")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            age = int(input("Enter age: "))
            phone = input("Enter phone number: ").strip()

            add_student(name, age, phone)

        elif choice == "2":
            print("\n--- Student List ---")
            get_students()

        elif choice == "3":
            name = input("Enter student name to update: ").strip()
            new_age = int(input("Enter new age: "))

            update_student(name, new_age)

        elif choice == "4":
            name = input("Enter student name to delete: ").strip()

            delete_student(name)

        elif choice == "5":
            name=input("Enter student name to search: ").strip()
            get_student_by_name(name)

        elif choice == "6":
            delete_all_students()


        elif choice == "7":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()