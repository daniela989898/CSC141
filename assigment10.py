# 10-1
filename = "learning_python.txt"
with open(filename, 'w') as file:
    file.write("In Python you can create variables easily.\n")
    file.write("In Python you can work with lists and dictionaries.\n")
    file.write("In Python you can build web applications, games, and AI models.\n")
with open(filename) as file:
    contents = file.read()
    print("=== Reading the entire file ===")
    print(contents)
with open(filename) as file:
    lines = file.readlines()
print("=== Reading line by line ===")
for line in lines:
    print(line.strip())
# 10-2
filename = "learning_python.txt"
with open(filename) as file:
    for line in file:
        new_line = line.replace('Python', 'C')
        print(new_line.strip())
# 10-3
filename = "learning_python.txt"
with open(filename) as file:
    contents = file.read()
    print("=== Reading the entire file ===")
    print(contents)
print("=== Reading line by line (simplified) ===")
with open(filename) as file:
    for line in file.read().splitlines():
        print(line)
# 10-4
guest_name = input("What is your name? ")
with open("guest.txt", "w") as file:
    file.write(guest_name)
print(f"Welcome, {guest_name}! Your name has been recorded.")
# 10-5
print("Enter your names. Type 'quit' to stop.")

with open("guest_book.txt", "w") as file:
    while True:
        name = input("Name: ")
        if name.lower() == "quit":
            break
        print(f"Welcome, {name}!")
        file.write(name + "\n")
# 10-6
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Please enter valid numbers only.")
else:
    print(f"The sum is {num1 + num2}.")
# 10-7
while True:
    print("Enter two numbers to add (or type 'q' to quit).")
    num1 = input("First number: ")
    if num1.lower() == 'q':
        break
    num2 = input("Second number: ")
    if num2.lower() == 'q':
        break
    try:
        result = int(num1) + int(num2)
    except ValueError:
        print("Please enter valid numbers only.")
    else:
        print(f"The sum is {result}.")
# 10-8
filenames = ["cats.txt", "dogs.txt"]
for file_name in filenames:
    try:
        with open(file_name) as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
    else:
        print(f"--- {file_name} ---")
        print(contents.strip())
# 10-9
filenames = ["cats.txt", "dogs.txt"]
for file_name in filenames:
    try:
        with open(file_name) as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        print(f"--- {file_name} ---")
        print(contents.strip())
# 10-10
filenames = ["book1.txt", "book2.txt", "book3.txt"]
for file_name in filenames:
    try:
        with open(file_name, encoding="utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    else:
        word_count = contents.lower().count("the ")
        print(f"The word 'the' appears about {word_count} times in {file_name}.")
# 10-11
import json
number = input("What is your favorite number? ")
filename = "favorite_number.json"
with open(filename, "w") as file:
    json.dump(number, file)
print("Your favorite number has been saved.")
# 10-12
import json
filename = "favorite_number.json"
try:
    with open(filename) as file:
        number = json.load(file)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open(filename, "w") as file:
        json.dump(number, file)
    print("Your favorite number has been saved.")
else:
    print(f"I know your favorite number! It’s {number}.")
# 10-13
import json
filename = "user_info.json"
user = {}
user["name"] = input("Enter your name: ")
user["age"] = input("Enter your age: ")
user["city"] = input("Enter your city: ")
with open(filename, "w") as file:
    json.dump(user, file)
with open(filename) as file:
    stored_user = json.load(file)
print(f"Your name is {stored_user['name']}, you are {stored_user['age']} years old, and you live in {stored_user['city']}.")
# 10-14
import json
filename = "username.json"
def get_new_username():
    username = input("What is your name? ")
    with open(filename, "w") as file:
        json.dump(username, file)
    return username
def greet_user():
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
    else:
        correct = input(f"Are you {username}? (y/n) ")
        if correct.lower() == "y":
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
greet_user()
