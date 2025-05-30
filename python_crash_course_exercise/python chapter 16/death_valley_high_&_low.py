from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt

path = Path('weather_data\death_valley_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, tmax, tmin = [], [] ,[]
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[6])
        low = int(row[7])
    except ValueError:
        print("Temperature was not Recorded")
    else:
        dates.append(current_date)
        tmax.append(high)
        tmin.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 5), dpi=110)
ax.plot(dates, tmax, linewidth=1/2, c="indigo", alpha=0.6)
ax.plot(dates, tmin, linewidth=1/2, c="orange", alpha=0.6)
ax.fill_between(dates, tmax, tmin, facecolor="purple", alpha=0.18)

# Labels format
ax.set_title("Daily High And Low Temperatue In Death_valley", fontsize=25)
ax.set_xlabel("Dates", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()
fig.align_labels()
ax.tick_params(labelsize=16)

plt.show()