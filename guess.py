#Write a program that generates a random number and allows the user to guess it.

import random
guess = int(input("Enter a Random Number For Guess Game:  "))
n=random.randrange(1,11)

while n!= guess:
    if guess>n:
        print("Too High !! Think Small any Number ")
        guess = int(input("Enter Again:  "))
    elif guess<n:
        print("Too low ! Think Any Big Number  ")
        guess = int(input("Enter Again:  "))
    else:
        break
print("Your Guess Number is  Right !")
