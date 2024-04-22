# """Guess the Number, by Geoffrey Geek
#Try to guess the secret number based on hints.
##View this code at my github respository Geoffrey Geek
## Tags: tiny, game##

import random

def askForGuess():
    while True:
        try:
            guess = int(input("Guess the number: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    secretNumber = random.randint(1, 100)
    for i in range(30):
        guess = askForGuess()
        if guess == secretNumber:
            print(f"Congratulations! You guessed the number {secretNumber} correctly!")
            break
        elif guess < secretNumber:
            print(f"Too low! Try again. The number is {secretNumber}.")
        else:
            print(f"Too high! Try again. The number is {secretNumber}.")
    else:
        print(f"Game over! The number was {secretNumber}.")

if __name__ == "__main__":
    main()