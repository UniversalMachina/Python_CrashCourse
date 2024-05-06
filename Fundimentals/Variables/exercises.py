# Exercise 1: Basic Arithmetic Operations
# This script asks the user to enter two numbers and prints the sum, difference, product, and quotient of those numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)

# Exercise 2: List Operations
# Asks the user to input a list of numbers and calculates the sum and average of these numbers.
numbers = input("Enter at least five numbers, separated by spaces: ").split()
numbers = [float(num) for num in numbers]
print("Sum of numbers:", sum(numbers))
print("Average of numbers:", sum(numbers) / len(numbers))

# Exercise 3: Dictionary Lookup
# Manages translations of English words to Spanish. It allows the user to input English words and displays the Spanish translation.
translations = {
    "hello": "hola",
    "world": "mundo",
    "computer": "computadora",
    "programming": "programación"
}
word = input("Enter an English word to translate to Spanish: ").lower()
print("Spanish translation:", translations.get(word, "This word is not in the dictionary."))

# Exercise 4: Mad Libs Game
# Creates a Mad Libs story by asking the user to provide various words to fill in the blanks.
print("Welcome to Mad Libs! Provide the requested words to create your story.")
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun (plural): ")
verb_past_tense = input("Enter a verb (past tense): ")
adverb = input("Enter an adverb: ")
adjective2 = input("Enter another adjective: ")
story = f"""
One day, my {adjective1} friend and I decided to go to the movie theater. We saw a group of {noun1}
that {verb_past_tense} {adverb} through the mall. We got really {adjective2} and decided to leave.
"""
print("Here is your story:")
print(story)
