import random
import matplotlib.pyplot as plt

# Roll the dice twice, 20 times, and calculate averages
averages = []
for _ in range(20):
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    average = (roll_1 + roll_2) / 2
    averages.append(average)

plt.bar(range(1, 21), averages, color='skyblue')
plt.title("Averages of Dice Rolls")
plt.xlabel("Attempt")
plt.ylabel("Average Value")
plt.xticks(range(1, 21))  # Display 1 to 20 on the x-axis
plt.savefig("plots/averages_plot.png")  # Save the plot as a PNG file
print("Plot saved as 'averages_plot.png'.")
