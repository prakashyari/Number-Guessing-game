import random
secret_number =random.randint(1,10)
print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 10. Can you guess it?")
while True:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number!")
        break