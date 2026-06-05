# =========================================
# FILE HANDLING MASTER PRACTICE
# =========================================


# -----------------------------------------
# 1. WRITE MODE ("w")
# -----------------------------------------
# Creates file if not present
# Deletes old content if file already exists

with open("sample1.txt", "w") as f:

    print("File Name :", f.name)
    print("File Mode :", f.mode)
    print("Is Closed :", f.closed)

    f.write("Hello World\n")
    f.write("I am Yashraj Sharma\n")
    f.write("Learning Python File Handling\n")

print("\nData written successfully.\n")


# -----------------------------------------
# 2. READ ENTIRE FILE
# -----------------------------------------

with open("sample1.txt", "r") as f:

    content = f.read()

    print("----- FULL FILE CONTENT -----")
    print(content)


# -----------------------------------------
# 3. READ SPECIFIC CHARACTERS
# -----------------------------------------

with open("sample1.txt", "r") as f:

    print("First 5 Characters:")
    print(f.read(5))

    print("\nCurrent Cursor Position:")
    print(f.tell())  # tells current pointer location


# -----------------------------------------
# 4. SEEK() -> MOVE CURSOR
# -----------------------------------------

with open("sample1.txt", "r") as f:

    f.seek(6)

    print("\nAfter seek(6):")
    print(f.read())


# -----------------------------------------
# 5. READ LINE BY LINE
# -----------------------------------------

with open("sample1.txt", "r") as f:

    print("\n----- READLINE() -----")

    print(f.readline())
    print(f.readline())


# -----------------------------------------
# 6. READLINES()
# -----------------------------------------

with open("sample1.txt", "r") as f:

    lines = f.readlines()

    print("\n----- READLINES() -----")

    print(lines)


# -----------------------------------------
# 7. LOOP THROUGH FILE
# -----------------------------------------

with open("sample1.txt", "r") as f:

    print("\n----- LOOPING FILE -----")

    for line in f:
        print(line.strip())


# -----------------------------------------
# 8. APPEND MODE ("a")
# -----------------------------------------
# Adds content at END of file

with open("sample1.txt", "a") as f:

    f.write("\nThis line is appended.")
    f.write("\nPython is powerful.")


print("\nNew Data Appended.\n")


# -----------------------------------------
# 9. READ AFTER APPEND
# -----------------------------------------

with open("sample1.txt", "r") as f:

    print("----- UPDATED FILE -----")
    print(f.read())


# -----------------------------------------
# 10. r+ MODE (READ + WRITE)
# -----------------------------------------

with open("sample1.txt", "r+") as f:

    print("\nCurrent Pointer:", f.tell())

    f.write("START-> ")

    f.seek(0)

    print("\n----- AFTER r+ WRITE -----")
    print(f.read())


# -----------------------------------------
# 11. FILE POINTER MOVEMENT
# -----------------------------------------

with open("sample1.txt", "r") as f:

    print("\nPointer:", f.tell())

    f.read(10)

    print("After Reading 10 chars:", f.tell())

    f.seek(0)

    print("After seek(0):", f.tell())


# -----------------------------------------
# 12. CHECK FILE PROPERTIES
# -----------------------------------------

with open("sample1.txt", "r") as f:

    print("\n----- FILE PROPERTIES -----")

    print("Name :", f.name)
    print("Mode :", f.mode)
    print("Readable :", f.readable())
    print("Writable :", f.writable())
    print("Closed :", f.closed)

print("Closed After with :", f.closed)


# =========================================
# END
# =========================================


import os

os.remove("sample1.txt")
