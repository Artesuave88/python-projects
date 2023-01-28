import random

# Generate a random number between 1 and 100
answer = random.randint(1, 100)

# Prompt the user to guess the number
guess = int(input("Guess a number between 1 and 100: "))

# Keep track of the number of guesses
count = 1

# Start the guessing loop
while guess != answer:
    if guess < answer:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
    guess = int(input("Guess a number between 1 and 100: "))
    count += 1

# Let the user know they have won
print("You got it! The number was", answer)
print("It took you", count, "guesses.")
