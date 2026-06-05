# Lists

fruits = ["Apple", "Orange", "Banana"]

for fruit in fruits:
    print(fruit)

fruits.append("Mango")
fruits.extend(["Watermelon", "Grapes"])

print(fruits)


# Dictionary

user = {
    "name": "Yashraj Sharma",
    "age": 21,
    "role": "Python Trainee",
}

for key, value in user.items():
    print(f"{key}: {value}")

user["email"] = "abcd@gmail.com"
user["mobile"] = "8989898988"

print(user)


# Tuple

states = ("Gujarat", "Rajasthan", "Haryana", "Delhi")

print(states)

# Tuples are immutable
# states[0] = "Punjab"  # TypeError


# Sets

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print(a.union(b))

print(a & b)
print(a - b)


# Tuple as dictionary key

key_tuple = (1, 2, 3)

sample_dict = {key_tuple: "Yashraj"}

print(sample_dict)

# Lists cannot be dictionary keys because they are mutable
# key_list = [1, 2, 3]
# sample_dict = {key_list: "Yashraj"}
