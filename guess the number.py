
import random

guess = random.randint(1, 100)

while True:
    try:
        ask = int(input("Guess the number between 1 and 100: ") )
        if guess == ask:
            print("Congracts")
            break
        elif guess > ask :
            print("Too high")
        elif guess < ask:
            print("Too low")
        else :
            print("Invalid")
    except ValueError:
        print("Invalid")
        
