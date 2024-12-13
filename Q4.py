# Write a program where the user has to guess a predefined number. Use a while loop to keep asking until they guess correctly, and provide hints if the guess is too high or too low.

import random

# Predefined number (you can also use random.randint for a random number)
number_to_guess = random.randint(1, 100)  # Random number between 1 and 100

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100. Can you guess what it is?")

# Initialize the variable for user input
user_guess = None

# Loop until the user guesses correctly
while user_guess != number_to_guess:
    try:
        # Get user input
        user_guess = int(input("Enter your guess: "))

        # Provide feedback
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number.")
    except ValueError:
        print("Please enter a valid integer.")
