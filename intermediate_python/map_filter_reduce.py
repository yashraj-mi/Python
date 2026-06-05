from functools import reduce

students = [
    {"name": "Amit", "marks": 85, "age": 20},
    {"name": "Priya", "marks": 42, "age": 19},
    {"name": "Rahul", "marks": 73, "age": 21},
    {"name": "Sneha", "marks": 91, "age": 22},
    {"name": "Karan", "marks": 35, "age": 20},
]

# Students with marks > 50
passed_students = list(filter(lambda student: student["marks"] > 50, students))
print(passed_students)

# Student names in uppercase
upper_names = list(map(lambda student: student["name"].upper(), students))
print(upper_names)

# Average marks
total_marks = reduce(
    lambda total, student: total + student["marks"],
    students,
    0,
)
print(total_marks / len(students))

# Names of students who passed
passed_names = list(
    map(
        lambda student: student["name"],
        filter(lambda student: student["marks"] >= 50, students),
    )
)
print(passed_names)

# Sum of marks of passed students
passed_marks_sum = reduce(
    lambda total, student: total + student["marks"],
    filter(lambda student: student["marks"] >= 50, students),
    0,
)
print(passed_marks_sum)

# Topper name using reduce only
topper = reduce(
    lambda student1, student2: (
        student1 if student1["marks"] > student2["marks"] else student2
    ),
    students,
)

print(topper["name"])
