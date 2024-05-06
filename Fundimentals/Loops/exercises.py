# Exercise 1: Count Down
# Description: Write a function that prints a countdown from any given number to zero.
def count_down(start):
    for i in range(start, -1, -1):
        print(i)

# Test the function
count_down(10)

# Exercise 2: Find the Maximum
# Description: Write a function that takes a list of numbers and returns the largest number using a loop.
def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Test the function
print(find_maximum([4, 11, 42, 3, 59, 27]))

# Exercise 3: Multiplication Table
# Description: Write a function that prints the multiplication table for a given number up to 10.
def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Test the function
multiplication_table(5)

# Exercise 4: Even Numbers in Range
# Description: Write a function that prints all even numbers from a starting to an ending number.
def print_even(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number)

# Test the function
print_even(1, 20)

# Exercise 5: Higher or Lower Game (Revised)
# Description: Modify the previous game to limit the number of guesses to 5.
import random

def higher_or_lower_revised():
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    print("Guess the number I'm thinking of between 1 and 100. You have 5 attempts.")

    while attempts < max_attempts:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        if user_guess < target:
            print("Higher...")
        elif user_guess > target:
            print("Lower...")
        else:
            print(f"Congratulations! You've guessed the number {target} in {attempts} attempts.")
            break

    if attempts >= max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {target}.")

# Call the game function to start the game
higher_or_lower_revised()
