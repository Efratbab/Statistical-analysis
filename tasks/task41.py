import random

# Roll the dice twice
roll_1 = random.randint(1, 6)
roll_2 = random.randint(1, 6)

# Calculate the average
average = (roll_1 + roll_2) / 2

# Print the results
print(f"First roll: {roll_1}")
print(f"Second roll: {roll_2}")
print(f"Sample average: {average}")
