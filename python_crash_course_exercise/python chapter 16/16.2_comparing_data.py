from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt
import mplcursors

path_1 = Path('weather_data/tokyo.csv')
lines_1 = path_1.read_text().splitlines()
reader_1 = csv.reader(lines_1)
hearder_row1 = next(reader_1)

path_2 = Path('weather_data\osaka.csv')
lines_2 = path_2.read_text().splitlines()
reader_2 = csv.reader(lines_2)
hearder_row2 = next(reader_2)

dates_1, tmin_1, tavg_1 = [], [], []
dates_2, tmin_2, tavg_2 = [], [], []

for row in reader_1:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        tmin = int(row[7])
        tavg = int(row[5])
        dates_1.append(current_date)
        tmin_1.append(tmin)
        tavg_1.append(tavg)
    except:
        continue

for row in reader_2:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        tmin = int(row[6])
        tavg = int(row[4])
        dates_2.append(current_date)
        tmin_2.append(tmin)
        tavg_2.append(tavg)
    except:
        continue

plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(10,5), dpi=100)
line_1 = ax.plot(dates_1, tmin_1, label="Tmin_tokyo", c="blue", alpha=0.3, linewidth=1, marker="o")[0]
line_2 = ax.plot(dates_1, tavg_1, label="Tavg_tokyo", c="indigo", alpha=0.3, linewidth=1, marker='v')[0]
line_3 = ax.plot(dates_2, tmin_2, label="Tmin_osaka", c="red", alpha=0.3, linewidth=1, marker='.')[0]
line_4 = ax.plot(dates_2, tavg_2, label="Tavg_osaka", c="orange", alpha=0.3, linewidth=1, marker='^')[0]

# Modifing the labels
ax.set_title("Data Comparision TOKYO & OSAKA", fontsize=24)
ax.set_xlabel("TIME", fontsize=14)
ax.set_ylabel("TEMPERATURE (F)", fontsize=14)
ax.tick_params(labelsize=16)
ax.legend(loc='best', title="Lines")

fig.autofmt_xdate()
fig.align_labels()

mplcursors.cursor([line_1, line_2, line_3, line_4], hover=True)

plt.show()
plt.savefig("graph")