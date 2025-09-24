# 1
car = 'subaru'
color = 'red'
number = 10
animal = 'dog'
fruit = 'apple'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs color == 'red'? I predict True.")
print(color == 'red')
print("\nIs number > 5? I predict True.")
print(number > 5)
print("\nIs animal == 'dog'? I predict True.")
print(animal == 'dog')
print("\nIs fruit in ['apple', 'banana', 'orange']? I predict True.")
print(fruit in ['apple', 'banana', 'orange'])
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\nIs color == 'blue'? I predict False.")
print(color == 'blue')
print("\nIs number < 5? I predict False.")
print(number < 5)
print("\nIs animal == 'cat'? I predict False.")
print(animal == 'cat')
print("\nIs fruit not in ['apple', 'banana', 'orange']? I predict False.")
print(fruit not in ['apple', 'banana', 'orange'])
# 2
car = "Subaru"
color = "Blue"
print("Is car == 'Subaru'? I predict True.")
print(car == "Subaru")
print("\nIs car == 'Toyota'? I predict False.")
print(car == "Toyota")
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == "subaru")
print("\nIs color.lower() == 'red'? I predict False.")
print(color.lower() == "red")
age = 18
score = 75
print("\nIs age == 18? I predict True.")
print(age == 18)
print("\nIs age != 18? I predict False.")
print(age != 18)
print("\nIs score > 50? I predict True.")
print(score > 50)
print("\nIs score < 50? I predict False.")
print(score < 50)
print("\nIs age >= 18? I predict True.")
print(age >= 18)
print("\nIs age <= 17? I predict False.")
print(age <= 17)
has_license = True
has_car = False
print("\nIs has_license and age >= 18? I predict True.")
print(has_license and age >= 18)
print("\nIs has_car and age >= 18? I predict False.")
print(has_car and age >= 18)
print("\nIs has_license or has_car? I predict True.")
print(has_license or has_car)
print("\nIs age < 18 or has_car? I predict False.")
print(age < 18 or has_car)
fruits = ["apple", "banana", "orange"]
print("\nIs 'apple' in fruits? I predict True.")
print("apple" in fruits)
print("\nIs 'grape' in fruits? I predict False.")
print("grape" in fruits)
print("\nIs 'grape' not in fruits? I predict True.")
print("grape" not in fruits)
print("\nIs 'banana' not in fruits? I predict False.")
print("banana" not in fruits)
# 3
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
    alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
# 4 
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points!")
alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points!")
# 5 
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")
alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")
# 6
age = 18
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
# 7
favorite_fruits = ["apple", "banana", "mango"]
if "apple" in favorite_fruits:
    print("You really like apples!")
if "banana" in favorite_fruits:
    print("You really like bananas!")
if "mango" in favorite_fruits:
    print("You really like mangoes!")
if "strawberry" in favorite_fruits:
    print("You really like strawberries!")
if "orange" in favorite_fruits:
    print("You really like oranges!")
# 8
usernames = ["lucia", "matias", "sofia", "mikel", "lucas"]
for user in usernames:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
# 9
usernames = []
if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
# 10
current_users = ["john", "sarah", "mike", "emma", "admin"]
new_users = ["JOHN", "chris", "sarah", "anna", "lucas"]
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a new one.")
    else:
        print(f"The username '{new_user}' is available.")
# 11 
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
# 12 
age = 20
user = "admin"
alien_color = "green"
if age < 13:
    print("Kid")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
if user == "admin":
    print("Hello admin, would you like to see a status report?")
else:
    print(f"Hello {user.title()}, welcome back!")
if alien_color.lower() == "green":
    print("The alien is green!")
# 13
current_users = ["admin", "john", "sarah", "mike"]

# Usuario que intenta loguearse
username = input("Enter your username: ")

# Verificación de login
if username.lower() in [user.lower() for user in current_users]:
    if username.lower() == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, welcome back!")
    print("\nLet's play a guessing game!")
    secret_number = 7
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("🎉 Correct! You earned 10 points!")
    elif guess < secret_number:
        print("Too low! You earned 5 points.")
    else:
        print("Too high! You earned 5 points.")
else:
    print("We need to find some users! (Invalid login)")