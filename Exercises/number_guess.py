import random

range=int(input("Enter a Range: "))

val = random.randint(1, range)


count = 0
while True:
    inp = int(input("Enter a Number: "))

    if val < inp:
        print("Guess  Small")
        count += 1
    elif val > inp:
        print("Guess  Big")
        count += 1
    else:
        print(f"Congrats!, You Guess the Number with {count+1} attempts!!")
        break
