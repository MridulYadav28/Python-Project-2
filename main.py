import random

def guess_number():
    n = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0  # Initialize the attempts counter

    while True:
        guess = int(input("Guess the number: "))  # Ask the user to input a guess
        attempts += 1  # Increment the attempts counter

        if guess < n:
            print("Higher number please")  # Provide feedback to guess higher
        elif guess > n:
            print("Lower number please")  # Provide feedback to guess lower
        else:
            print(f"You have guessed the number {n} correctly in {attempts} attempts")  # Display success message
            break  # Exit the loop when the correct number is guessed

guess_number()  # Call the function to start the number guessing game
