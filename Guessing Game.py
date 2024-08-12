import random

x = input("Input any values: ")

if x == str:
    while True:
        print("Let's play a guessing game")
        l = input("Enter a single character: ")
        if l == random:
            print("Congratulations!!! You Won")
        else:
            guess = 5
            print("Wrong letter")
            print(f"You have {5} guesses left")
            