# Exercise 1: Using the math Module
# Description: Write a program that uses functions from the math module to perform various mathematical operations.
import math

# Use math.sqrt to calculate the square root of a number
print("Square root of 16 is:", math.sqrt(16))

# Use math.pow to calculate the power of numbers
print("3 raised to the power of 4 is:", math.pow(3, 4))

# Use math.pi to print the value of pi
print("Value of pi is:", math.pi)

# Use math.cos to find the cosine of a radian value
print("Cosine of pi is:", math.cos(math.pi))

# Exercise 2: Working with the datetime Module
# Description: Write a program that prints the current date, and then prints a date two weeks from the current date.
import datetime

# Get today's date
today = datetime.date.today()
print("Today's date is:", today)

# Calculate the date two weeks from today
two_weeks = datetime.timedelta(weeks=2)
future_date = today + two_weeks
print("Two weeks from now will be:", future_date)

# Exercise 3: Using the random Module
# Description: Create a program that generates and prints a random integer between 1 and 100, and then picks a random element from a list.
import random

# Generate a random integer
random_int = random.randint(1, 100)
print("A random integer between 1 and 100:", random_int)

# Pick a random element from a list
colors = ["red", "blue", "green", "yellow"]
random_color = random.choice(colors)
print("A random color from the list:", random_color)

# Exercise 4: Exploring the os Module
# Description: Write a script that prints your current working directory and lists all files and directories in it.
import os

# Print the current working directory
print("Current working directory:", os.getcwd())

# List all files and directories in the current directory
print("Contents of the directory:", os.listdir())

# Exercise 5: Create Your Own Module
# Description: Create a simple Python module named greetings.py that contains functions to print "hello" and "goodbye". Then, write a script to import and use these functions.
# First, create greetings.py:
# File: greetings.py
# def say_hello(name):
#     print(f"Hello, {name}!")
# def say_goodbye(name):
#     print(f"Goodbye, {name}!")

# Then, use the module:
# Assuming greetings.py is created and accessible
# import greetings
# Use functions from the greetings module
# greetings.say_hello("Alice")
# greetings.say_goodbye("Bob")
