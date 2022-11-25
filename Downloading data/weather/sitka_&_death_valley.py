import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename_s = 'sitka_weather_2014.csv'
with open(filename_s) as f_s:
    reader = csv.reader(f_s)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates_s, highs_s, lows_s = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        try:
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates_s.append(current_date)
            highs_s.append(high)
            lows_s.append(low)

filename_dv = 'death_valley_2014.csv'
with open(filename_dv) as f_d:
    reader = csv.reader(f_d)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates_d, highs_d, lows_d = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        try:
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates_d.append(current_date)
            highs_d.append(high)
            lows_d.append(low)

# Plot the high and low temperatures in Sitka.
plt.style.use('classic')
fig, ax = plt.subplots(dpi=128, figsize=(12, 7))
ax.plot(dates_s, highs_s, c='red', alpha=0.1)
ax.plot(dates_s, lows_s, c='blue', alpha=0.1)
ax.fill_between(dates_s, highs_s, lows_s, facecolor='green', alpha=0.3)
# Plot the high and low temperatures in Death Valley.
ax.plot(dates_d, highs_d, c='red', alpha=0.5)
ax.plot(dates_d, lows_d, c='blue', alpha=0.5)
ax.fill_between(dates_d, highs_d, lows_d, facecolor='brown', alpha=0.3)
# Format plot.
title = "Daily high and low temperatures - Sitka and Death Valley"
ax.set_title(title, fontsize=14)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=10)
plt.ylim(0, 130)
plt.savefig('sitka_&_death_valley.png')


plt.show()
