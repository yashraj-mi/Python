import math


def greetings(name):
    print(f"Welcome, {name}!")


greetings("Yashraj")


# =================================================


def factorial(number):
    if number < 0:
        return -1

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact


print(factorial(3))


# =============================================


def isPalindrome(str):
    str_list = [c for c in str]

    i = 0
    j = len(str) - 1

    while i < j:
        if str_list[i] != str_list[j]:
            return False

        i += 1
        j -= 1

    return True


print(isPalindrome("yashsay"))

# ========================================================


def calculate_area(radius):
    return round(math.pi * (radius**2), 2)


print(calculate_area(3.1))
