# Print Function in Python


# Print a string containing quotes inside it
print('He said, "Python is awesome!"')

# Print multiple values separated by commas
print("Name:", "John", "Age:", 25)

# Use end parameter
print("Hello", end=" ")
print("World")


# Syntax


# Print welcome message
print("Welcome to Python Programming!")

# Fixed syntax errors
print("Hello World")

name = input("Enter your name: ")
print("Hello,", name)

# Multi-line string
print("""
This is a multi-line string.
Python makes it easy
to print multiple lines.
""")


# Comments


length = 10

width = 5

area = length * width

# Display area
print("Area of Rectangle:", area)


def greet():
    """
    This function prints a greeting message.
    """
    print("Welcome!")


greet()

# Disabled code using comment
# print("This line is disabled")


# Variables


# Different data types
integer_var = 100
float_var = 99.99
string_var = "Python"
bool_var = True

print(integer_var)
print(float_var)
print(string_var)
print(bool_var)

# Swap two numbers without third variable
a = 10
b = 20

print("Before Swap:", a, b)

a, b = b, a

print("After Swap:", a, b)

# Multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)


# Data Types


print(type(10))
print(type(3.14))
print(type("Hello"))
print(type(True))

# Integer to string
num = 100
text = "Score: " + str(num)
print(text)

# Check if integer
value = 50
print(isinstance(value, int))


# Numbers


num1 = 15
num2 = 4

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Remainder
print("Remainder:", num1 % num2)

# Even or Odd
number = int(input("Enter a number to check Even/Odd: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


#  Strings


user_string = input("Enter a string: ")

# Length
print("Length:", len(user_string))

# Case conversions
print("Upper:", user_string.upper())
print("Lower:", user_string.lower())
print("Capitalize:", user_string.capitalize())

# Replace Python with Java
sample = "I love Python. Python is easy."
print(sample.replace("Python", "Java"))


# Booleans


print(10 > 5)
print(3 == 3)

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

a = True
b = False

print("AND:", a and b)
print("OR:", a or b)
print("NOT:", not a)


# Operators


a = 12
b = 5

# Arithmetic Operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a**b)

# Comparison Operators
print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)

# Logical Operators
print((a > 10) and (b > 2))
print((a < 10) or (b > 2))
print(not (a > b))


# Type Casting


num = 123
print("Number: " + str(num))

value = "123.45"

float_value = float(value)
int_value = int(float_value)

print(float_value)
print(int_value)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("Sum =", n1 + n2)


# Printing & Getting Input


print("My", "name", "is", "Python")

user = input("Enter your name: ")
print("Hello,", user)

number = int(input("Enter a number: "))
print("Square =", number**2)


# String Formatting


name = "Alice"
age = 25

# f-string
print(f"My name is {name} and I am {age} years old.")

# format()
print("My name is {} and I am {} years old.".format(name, age))

# Two decimal places
PI = 3.14159265
print(f"{PI:.2f}")


# String Methods


sentence = "Python programming is fun"

# Contains specific word
print("Python" in sentence)

# Count occurrences
print(sentence.count("m"))

# Reverse string
print(sentence[::-1])


# Lists


fruits = ["Apple", "Banana", "Mango"]

print(fruits)

# Add element
fruits.append("Orange")
print(fruits)

# Remove element
fruits.remove("Banana")
print(fruits)

# Sort list
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)


# Tuples


colors = ("Red", "Green", "Blue")

# Access elements
print(colors[0])

# Convert tuple to list
color_list = list(colors)
color_list.append("Yellow")

print(color_list)

# Check value exists
print("Green" in colors)


# Sets


set1 = {1, 2, 3}

# Add element
set1.add(4)
print(set1)

# Intersection
set2 = {3, 4, 5}
print(set1.intersection(set2))

# Remove element
set1.remove(2)
print(set1)


# Dictionaries


student = {"name": "Yashraj", "age": 21, "course": "Python"}

# Print keys and values
print("Keys:", student.keys())
print("Values:", student.values())

# Add key-value pair
student["city"] = "Ahmedabad"
print(student)

# Remove key-value pair
student.pop("age")
print(student)

# Merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = dict1 | dict2
print(merged)
