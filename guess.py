# Guess the Number Game
import random

print("🎮 Guess the Number Game")
number = random.randint(1, 30)   # computer picks a number
attempts = 0

while True:
    guess = int(input("Enter your guess (1-30): "))
    attempts += 1

    if guess == number:
        print(f"🎉 Correct! You guessed it in {attempts} attempts!")
        break
    elif guess < number:
        print("🔼 Too low! Try again.")
    else:
        print("🔽 Too high! Try again.")