from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt
import mplcursors

path = Path('weather_data\sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

date, pcrpt = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    pcrp = float(row[5])
    date.append(current_date)
    pcrpt.append(pcrp)

plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(10, 5), dpi=120)
line = ax.plot(date, pcrpt, c="pink", alpha=0.7, linewidth=2, marker="o", label="Sitka Precipitate")[0]
ax.set_title("Daily Precipitate Data", fontsize=24)
ax.set_xlabel("Time", fontsize=16)
ax.set_ylabel("Precipitate", fontsize=16)
ax.legend(loc="best", title="Sitka", fontsize=16)

cursor = mplcursors.cursor([line], hover=True)

plt.show()