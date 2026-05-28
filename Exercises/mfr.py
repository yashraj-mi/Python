# nums=[1,2,3,4,5,6,7,8,9,10]

# squares=list(map(lambda x:x*x,nums))
# print(squares)


# filtered_squares=list(filter(lambda x:x>25,squares))
# print(filtered_squares)



from functools import reduce
# sum_of_squares=reduce(lambda acc,b:acc + b,squares)
# print(sum_of_squares)





students = [
    {"name": "Amit", "marks": 85, "age": 20},
    {"name": "Priya", "marks": 42, "age": 19},
    {"name": "Rahul", "marks": 73, "age": 21},
    {"name": "Sneha", "marks": 91, "age": 22},
    {"name": "Karan", "marks": 35, "age": 20},
]

# Get all students who scored more than 50 marks.

print(list(filter(lambda x:x["marks"]>50,students)))

# Create a new list containing only student names in uppercase.

print(list(map(lambda x: x["name"].upper(),students)))


# Find average marks of all students.

total_marks=reduce(lambda acc,x:acc+x["marks"],students,0)
print(total_marks/len(students))


# Get names of students who passed (marks >= 50).
print(list(map(lambda x:x["name"],filter(lambda x:x["marks"]>=50,students))))

# Find sum of marks of only passed students.
print(reduce(lambda acc,x:acc+x["marks"],filter(lambda x: x["marks"]>=50,students),0))

# Find the topper student name using reduce() only.

print(reduce(lambda a,b:a if a["marks"]>b["marks"] else b,students)["name"])

