from db import students

def add_student(name: str, age: int, phone: str) -> None:
    """Add a new student to the database."""
    result = students.insert_one({
        "name": name,
        "age": age,
        "phone": phone
    })
    print(f"Student added successfully. ID: {result.inserted_id}")

def get_students() -> None:
    """Retrieve and display all students."""
    student_list = list(students.find())

    if not student_list:
        print("No students found.")
        return

    for student in student_list:
        print(student)


def get_student_by_name(name: str) -> None:
    """Find and display a student by name."""
    student = students.find_one({"name": name})

    if student:
        print(student)
    else:
        print("Student not found.")


def update_student(name: str, age: int) -> None:
    """Update the age of a student identified by name."""
    result = students.update_one(
        {"name": name},
        {"$set": {"age": age}}
    )

    if result.matched_count:
        print("Student updated successfully.")
    else:
        print("Student not found.")


def delete_student(name: str) -> None:
    """Delete a student by name."""
    result = students.delete_one({"name": name})

    if result.deleted_count:
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def delete_all_students() -> None:
    """Delete all students from the database."""
    result = students.delete_many({})
    print(f"{result.deleted_count} students deleted.")


def search_students_by_age(age: int) -> None:
    """Search for and display students with a specific age."""
    result = students.find({"age": age})

    found = False
    for student in result:
        print(student)
        found = True

    if not found:
        print("No students found.")