import csv
from matplotlib import pyplot as plt
from datetime import datetime


# Get dates, high and low temperatures from file.
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)
print(dates)
# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# Format plot.
fig.autofmt_xdate()
plt.title('Daily high and low temperatures - 2014', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature(°C)", fontsize=16)
plt.tick_params(axis='y', which='major', labelsize=16)

# Show plot.
plt.show()


    # print(header_row)

    # for index, column_header in enumerate(header_row):
        # print(index, column_header)
