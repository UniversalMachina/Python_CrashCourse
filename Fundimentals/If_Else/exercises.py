# Exercise 1: Simple Conditions
# Description: Write a Python function that checks if a number is positive, negative, or zero.
def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

# Test the function
check_number(10)
check_number(-5)
check_number(0)

# Exercise 2: Eligibility for Voting
# Description: Create a function that determines if a person is eligible to vote based on their age.
def can_vote(age):
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")

# Test the function
can_vote(20)
can_vote(16)

# Exercise 3: Grading System
# Description: Implement a function that assigns a grade to a score according to the academic grading system.
def assign_grade(score):
    if score >= 90:
        print("Grade A")
    elif score >= 80:
        print("Grade B")
    elif score >= 70:
        print("Grade C")
    elif score >= 60:
        print("Grade D")
    else:
        print("Grade F")

# Test the function
assign_grade(88)
assign_grade(74)
assign_grade(59)

# Exercise 4: Choose Your Own Adventure Game
# Description: Create a simple text-based "choose your own adventure" game that makes use of nested if statements.
print("Welcome to your adventure!")
choice1 = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if choice1 == "left":
    choice2 = input("You've come to a river, you can walk around it or swim across? Type 'walk' to walk around and 'swim' to swim across: ").lower()
    if choice2 == "swim":
        print("You swam across and were eaten by an alligator.")
    elif choice2 == "walk":
        print("You walked for many miles, ran out of water, and lost the game.")
    else:
        print("Invalid choice. Game over.")

elif choice1 == "right":
    choice2 = input("You've come to a bridge, it looks wobbly, would you like to cross it or head back (cross/back)? ").lower()
    if choice2 == "back":
        print("You go back and lose because you are out of options.")
    elif choice2 == "cross":
        choice3 = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
        if choice3 == "yes":
            print("You talk to the stranger and they give you a treasure. You win!")
        elif choice3 == "no":
            print("You ignore the stranger and they are offended and steal all your belongings. You lose.")
        else:
            print("Invalid choice. Game over.")
    else:
        print("Invalid choice. Game over.")
else:
    print("Invalid choice. Game over.")
