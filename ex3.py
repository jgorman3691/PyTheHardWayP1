#!/usr/bin/env python3

# This line prints out the first line of the program
print("I will now count my chickens:")

# These two lines print out the amount of hens and roosters.  The division with a single slash makes it a float, a double slash would keep it an int
print("Hens", float(25 + 30 / 6))
print("Roosters", float(100 - 25 * 3 % 4))

# Another print statement
print("Now I will count the eggs:")

# This print statement calculates the total amount of eggs.  There is no string inside to print
print(float(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6))

# This asks a question
print("Is it true that 3 + 2 < 5 - 7?")

# This calculates the previous question and answers it as a boolean statement
print((3 + 2 < 5 - 7))

# These two statements have a string asking the question, and then a boolean expression afterwards
print("What is 3 + 2?", float(3 + 2))
print("What is 5 - 7?", float(5 - 7))

# No fucking duh
print("Oh, that's why it's False.")

# I fucking hate you
print("How about some more.")

# These three statements repeat the previous sentences that have a string followed by a boolean expression
print("Is it greater?", (5 > -2))
print("Is it greater or equal?", (5 >= -2))
print("Is it less or equal?", 5 <= -2)
