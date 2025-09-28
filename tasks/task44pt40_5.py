import random
import matplotlib.pyplot as plt

# Roll the dice 5 times, 40 times, and calculate averages
averages = []
for _ in range(40):
    rolls = [random.randint(1, 6) for _ in range(5)]  # Generate 5 dice rolls
    average = sum(rolls) / len(rolls)  # Calculate the average of 5 rolls
    averages.append(average)

plt.bar(range(1, 41), averages, color='skyblue')
plt.title("Averages of 5 Dice Rolls")
plt.xlabel("Attempt")
plt.ylabel("Average Value")
plt.xticks(range(1, 41, 2))  # Display 1 to 40 on the x-axis with step of 2 for better spacing
plt.savefig("plots/averages_plot_40_rolls_5.png")  # Save the plot as a PNG file
print("Plot saved as 'averages_plot_40_rolls_5.png'.")
