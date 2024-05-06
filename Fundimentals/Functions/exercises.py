# Exercise 1: Temperature Converter
# Write a function that converts a temperature from Fahrenheit to Celsius.
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

# Test the function
print(fahrenheit_to_celsius(68))  # Should print the Celsius equivalent of 68 degrees Fahrenheit

# Exercise 2: Password Validator
# Create a function that checks if a password meets a simple set of rules: at least 8 characters long and contains both letters and numbers.
def validate_password(password):
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    return len(password) >= 8 and has_letter and has_number

# Test the function
print(validate_password("mypassword123"))  # Should return True
print(validate_password("short1"))  # Should return False

# Exercise 3: Prime Number Checker
# Develop a function to check if a number is prime.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test the function
print(is_prime(11))  # Should return True
print(is_prime(4))  # Should return False

# Exercise 4: Text Reverser
# Write a function that reverses the text provided to it.
def reverse_text(text):
    return text[::-1]

# Test the function
print(reverse_text("hello"))  # Should return "olleh"

# Exercise 5: Fibonacci Sequence
# Implement a function that returns the nth Fibonacci number.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Test the function
print(fibonacci(10))  # Should print the 10th Fibonacci number
