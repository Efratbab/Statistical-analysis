import random

# Roll the dice 5 times
rolls = [random.randint(1, 6) for _ in range(5)]

# Calculate the average
average = sum(rolls) / len(rolls)

# Print the results
for i, roll in enumerate(rolls, start=1):
    print(f"Roll {i}: {roll}")
print(f"Sample average: {average}")
