# Daniela 
from random import randint
answer = randint(1, 100)
guess = -1
while guess != answer:
    print("enter your guess")
    guess = input()
    guess= int(guess)
    if guess > answer:
        print("too high")
    elif guess < answer:
        print("too low")
print("You figured it over")