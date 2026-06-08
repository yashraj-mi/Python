# LOGICAL EXPRESSIONS

#Write a program that checks if a number is Positive, Negative or Zero.
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Compare three numbers and print the largest
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest = max(num1, num2, num3)
print(f"Largest number: {largest}")


# Check if a year is a leap year
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# IF-ELIF-ELSE

# Ask the user for their age and print if they are a minor or an adult.

age = int(input("Enter your age: "))

if age < 18:
    print("Minor")
else:
    print("Adult")


# Grading system
marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# Divisible by both 3 and 5
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")


# FOR LOOP

# Print numbers from 1 to 10
for num in range(1, 11):
    print(num)


# Sum of all even numbers up to 100
total = 0

for num in range(0, 101, 2):
    total += num

print(f"Sum of even numbers: {total}")


# Print each letter of a word on a new line
word = "Yashraj"

for letter in word:
    print(letter)


# WHILE LOOP

# Print numbers from 1 to 5
counter = 1

while counter <= 5:
    print(counter)
    counter += 1


# Keep taking input until user enters exit
while True:
    text = input("Enter text: ")

    if text.lower() == "exit":
        print("Program terminated.")
        break


# Fibonacci series up to n terms
terms = int(input("Enter number of terms: "))

first = 0
second = 1

if terms >= 1:
    print(first, end=" ")

if terms >= 2:
    print(second, end=" ")

count = 2

while count < terms:
    next_number = first + second
    print(next_number, end=" ")

    first = second
    second = next_number
    count += 1

print()



# BREAK, CONTINUE, PASS

# Break example
for num in range(1, 11):
    if num == 6:
        break

    print(num)


# Continue example
for num in range(1, 11):
    if num == 5:
        continue

    print(num)


# Pass example
def future_feature() -> None:
    """Placeholder function for future implementation."""
    pass


# FUNCTIONS

def square(number: int) -> int:
    """
    Return the square of a number.

    Args:
        number: Integer value.

    Returns:
        Square of the number.
    """
    return number * number


def greet(name: str) -> None:
    """
    Print a greeting message.

    Args:
        name: User's name.
    """
    print(f"Hello, {name}!")


def factorial(number: int) -> int:
    """
    Calculate factorial of a number.

    Args:
        number: Non-negative integer.

    Returns:
        Factorial value.
    """
    result= 1

    for value in range(1, number + 1):
        result *= value

    return result






# RETURN STATEMENTS

def add_numbers(first: int, second: int) -> int:
    """
    Return the sum of two numbers.

    Args:
        first: First integer.
        second: Second integer.

    Returns:
        Sum of the numbers.
    """
    return first + second


def is_prime(number: int) -> bool:
    """
    Check whether a number is prime.

    Args:
        number: Integer value.

    Returns:
        True if prime, otherwise False.
    """
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def is_palindrome(text: str) -> bool:
    """
    Check whether a string is a palindrome.

    Args:
        text: Input string.

    Returns:
        True if palindrome, otherwise False.
    """
    processed_text = text.lower()

    return processed_text == processed_text[::-1]





# LOCAL AND GLOBAL SCOPE

message = "Global Variable"


def show_scope() -> None:
    """
    Demonstrate local scope.
    """
    message = "Local Variable"
    print(message)


print(message)


# Modify global variable
counter = 0


def increment_counter() -> None:
    """
    Update the global counter variable.
    """
    global counter

    counter += 1


print(counter)

def main() -> None:
    """Execute function examples."""

    print(square(5))
    greet("Yashraj")
    print(factorial(5))

    print(add_numbers(10, 20))
    print(is_prime(17))
    print(is_palindrome("madam"))

    show_scope()
    print(message)

    print(counter)

    increment_counter()
    increment_counter()

    print(counter)


if __name__ == "__main__":
    main()