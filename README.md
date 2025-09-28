# Statistical Methods in Python – Dice Simulation

This project was created as part of the **Statistical Methods in Computer Science** course.  
It demonstrates concepts of probability and the Law of Large Numbers using **dice roll simulations** in Python.

---

## 📊 Project Overview

The tasks simulate rolling dice multiple times and calculating the **sample average**.  
Results are visualized with **bar charts** to show how averages stabilize as the number of rolls increases.

Key experiments:
- Rolling 2 dice and computing the average :contentReference[oaicite:0]{index=0}
- Repeating the experiment 20 times and plotting results :contentReference[oaicite:1]{index=1}
- Rolling 10 dice, repeated 40 times, and observing averages :contentReference[oaicite:2]{index=2}
- Rolling 5 or 10 dice with averages shown across multiple iterations :contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}

---

## 🗂 Project Structure
tasks/
task41.py # Roll 2 dice, compute sample average
task42.py # Repeat dice rolling 20 times and plot results
task44.py # Roll 10 dice, repeat 40 times, plot averages
task431_1.py # Roll 5 dice and calculate average
task431_2.py # Roll 5 dice, repeat 20 times, plot averages
task432_1.py # Roll 10 dice and calculate average
task432_2.py # Roll 10 dice, repeat 20 times, plot averages

plots/ # Saved PNG plots from matplotlib


---

## 🚀 How to Run
Clone the repository and install requirements:
```bash
git clone https://github.com/<your-username>/statistical-methods-dice-simulation.git
cd statistical-methods-dice-simulation
pip install -r requirements.txt

Run a task, for example:
python tasks/task42.py
