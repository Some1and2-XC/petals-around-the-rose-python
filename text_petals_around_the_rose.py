import random
diceRoll = 0
guessCorrect = 0
while guessCorrect != 10:
    diceTotal = 0
    guessLoop = True
    print("---")
    for i in range(1, 6):
        diceRoll = random.randint(1, 6)
        if diceRoll == 1:
            print()
            print(" x")
            print()
        elif diceRoll == 2:
            print("x")
            print()
            print("  x")
        elif diceRoll == 3:
            print("x")
            print(" x")
            print("  x")
            diceTotal += 2
        elif diceRoll == 4:
            print("x x")
            print()
            print("x x")
        elif diceRoll == 5:
            print("x x")
            print(" x")
            print("x x")
            diceTotal += 4
        elif diceRoll == 6:
            print("x x")
            print("x x")
            print("x x")
        print("---")
    while guessLoop is True:
        guess = input("What is your Guess?")
        guessLoop = False
        for i in guess:
            if 48 <= ord(i) <= 57:
                guessLoop = guessLoop
            else:
                guessLoop = True
        if guess == "":
            guessLoop = True
        if guessLoop is True:
            print("Invalid Input")
            print()
    guess = int(guess)
    if guess == diceTotal:
        print("*CORRECT*")
        guessCorrect += 1
    elif guess % 2 != 0:
        print("It's", diceTotal, "not", guess, "(the total is always even)")
        guessCorrect = 0
    else:
        print("It's", diceTotal, "not", guess)
        guessCorrect = 0
    input()