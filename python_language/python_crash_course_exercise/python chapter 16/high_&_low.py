from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data\sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines) 
header_row = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    avg = row[3]
    high = int(row[4]) # sting to number
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# plot the high temperature.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(11, 5), dpi=100)
ax.plot(dates, highs, c='purple', linewidth=1.2, alpha=0.5, label="Sitka High Temperature", marker="o")
ax.plot(dates, lows, c="green", linewidth=1, alpha=0.5, label="Sitka Low Temperature", marker=".")
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.17)

# Format plot
ax.set_title('Daily High and Low Temperature, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperature(F)', fontsize=16)

fig.autofmt_xdate()
fig.align_xlabels()
ax.tick_params(labelsize=16)
ax.legend(loc="best", title="Temperature", fontsize=16)

plt.show()