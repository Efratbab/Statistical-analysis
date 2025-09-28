import random
import matplotlib.pyplot as plt

# Perform the experiment 20 times and store averages
averages = []
for _ in range(20):
    rolls = [random.randint(1, 6) for _ in range(10)]  # Roll 10 dice
    average = sum(rolls) / len(rolls)  # Calculate average
    averages.append(average)

# Create a bar chart to visualize the averages
plt.bar(range(1, 21), averages, color='skyblue')  # 20 iterations
plt.title("Averages of 10 Dice Rolls (20 Iterations)")
plt.xlabel("Attempt")
plt.ylabel("Average Value")
plt.xticks(range(1, 21))  # Display 1 to 20 on the x-axis
plt.savefig("plots/averages_of_10_dice_rolls_20_iterations.png")  # Save the plot as PNG
print("Plot saved as 'averages_of_10_dice_rolls_20_iterations.png'.")
