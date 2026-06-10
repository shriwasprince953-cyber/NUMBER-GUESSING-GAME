import random

print("🎮 Welcome to Number Guessing Game")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("TOO LOW! 📉")

    elif guess > secret_number:
        print("TOO HIGH! 📈")

    else:
        print("🎉 CONGRATULATIONS..................")
        print(" BUT YOU GUESSED IT RIGHT", attempts, "attempts.")
        break