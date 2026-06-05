import math
from functools import reduce


def greet(name: str) -> None:
    """Print a welcome message for the given name."""
    print(f"Welcome, {name}!")


def factorial(number: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Raises:
        ValueError: If the input is negative.
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for value in range(1, number + 1):
        result *= value

    return result


def is_palindrome(text: str) -> bool:
    """Return True if the given string is a palindrome."""
    text = text.lower()
    return text == text[::-1]


import math


def calculate_area(radius: float) -> float:
    """
    Calculate the area of a Triangle.

    Raises:
        ValueError: If the radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    return round(math.pi * radius**2, 2)


def generate_numbers():
    """Generate numbers from 0 to 18."""
    yield from range(19)


def main() -> None:
    """Run all examples."""

    greet("Yashraj")

    try:
        print(factorial(3))
        print(factorial(-3))
    except ValueError as error:
        print(error)

    print(is_palindrome("yashsay"))

    try:
        print(calculate_area(3.1))
        (calculate_area(-2))
    except ValueError as error:
        print(error)

    strings = ["yashraj", "abcdcba", "AhrttRHA"]
    print(list(map(is_palindrome, strings)))

    numbers = list(range(50))

    print(list(filter(lambda number: number % 2 == 0, numbers)))

    print(reduce(lambda total, number: total + number, numbers, 0))

    generator = generate_numbers()

    print(next(generator))
    print(next(generator))
    print(next(generator))

if __name__ == "__main__":
    main()
