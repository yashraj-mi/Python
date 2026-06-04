# LIST


fruits = ["Apple", "Orange", "Banana"]

for fruit in fruits:
    print(fruit)

fruits.append("Mango")
fruits.extend(["Watermelon", "Graps"])

print(fruits)


# Dictionary

user = {"name": "Yashraj Sharma", "age": "21", "role": "Python Trainee"}

for key, value in user.items():
    print(f"{key}: {value}")

user["email"] = "abcd@gmail.com"
user["mobile"] = "8989898988"

print(user)


# tuple

states = ("Gujarat", "Rajasthan", "Haryana", "Delhi")

print(states)
# can not add or mutate tuples because it's immutable
# states[0]="HR" --->Gives Error


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)
print(A.union(B))

print(A & B)
print(A - B)
print(A)


key_tuple = (1, 2, 3)
key_list = [1, 2, 3]

sample_dict = {
    key_tuple: "Yashraj",  # it is valid because tuple is immutable
    key_list: "Yashraj",  # it's invalid because list is mutable
}
