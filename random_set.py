#!/usr/bin/env python3
# Unique Random Number Generator
# This Python program generates a specified number of unique random numbers within a given range
# and prints them in ascending order. It uses the `random` module to ensure randomness while preventing duplicates.

import random

# Define the range of random numbers
randomMin = 0
randomMax = 149

# Specify the number of unique random numbers to generate
randomCount = 33

# Create a set to store unique random numbers
unique_numbers = set()

# Continue generating random numbers until we have the desired count of unique numbers
while len(unique_numbers) < randomCount:
    # Generate a random number within the specified range
    random_number = random.randint(randomMin, randomMax)
    
    # Check if the random number is not in the set (i.e., it's unique)
    if random_number not in unique_numbers:
        unique_numbers.add(random_number)

# Sort the unique numbers in ascending order
sorted_numbers = sorted(unique_numbers)

# Print the unique numbers in ascending order
for number in sorted_numbers:
    print(f"Number: {number}")
