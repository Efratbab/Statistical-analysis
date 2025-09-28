import random

# Roll the dice 10 times
rolls = [random.randint(1, 6) for _ in range(10)]

# Calculate the average
average = sum(rolls) / len(rolls)

# Print the results
for i, roll in enumerate(rolls, start=1):
    print(f"Roll {i}: {roll}")
print(f"Sample average: {average}")
