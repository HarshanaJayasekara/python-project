import random

while True:
    ask = input("rolling y/n >").lower()
    if ask == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You roolled a {die1}and a {die2}.")
    elif ask== 'n':
        print("Thanks")
        break
    else:
        print("invalide")