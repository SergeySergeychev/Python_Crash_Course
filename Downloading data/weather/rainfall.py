import csv
from datetime import datetime
from matplotlib import pyplot as plt

def get_weather_data(filename, dates,  date_index, ele_index):
    """Get the precepitation level from a data file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get element data and dates.
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                element = float(row[ele_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                insp_elements.append(element)

# Get precipitation level per month in Sitka.
filename = 'sitka_weather_07-2014.csv'
dates, insp_elements = [], []
get_weather_data(filename, dates, date_index=0, ele_index=19)

plt.style.use('classic')
fig, (ax1, ax2, ax3) = plt.subplots(3, dpi=80, figsize=(11,7))
ax1.plot(dates, insp_elements, c='blue', alpha=0.6, linewidth=3)
ax1.fill_between(dates, insp_elements, facecolor='blue', alpha=0.4)
title = "Precipitation level in Sitka per July"
ax1.set_title(title, fontsize=14)
ax1.set_xlabel('', fontsize=10)
fig.autofmt_xdate()
ax1.set_ylabel("Precipitation in mm", fontsize=10)
ax1.set_ylim(0, 4)
ax1.tick_params(axis='y', which='minor', labelsize=10)

# Get precipitation level per year in Sitka
filename = 'sitka_weather_2014.csv'
dates, insp_elements = [], []
get_weather_data(filename, dates, date_index=0, ele_index=19)
ax2.plot(dates, insp_elements, c='blue', alpha=0.6, linewidth=3)
ax2.fill_between(dates, insp_elements, facecolor='blue', alpha=0.4)
# Format plot.
title = "Precipitation level in Sitka per year"
ax2.set_title(title, fontsize=14)
ax2.set_xlabel('', fontsize=10)
fig.autofmt_xdate()
ax2.set_ylabel("Precipitation in mm", fontsize=10)
ax2.tick_params(axis='y', which='minor', labelsize=10)

# Get Max wind speed limit in Sitka.
filename = 'sitka_weather_2014.csv'
dates, insp_elements = [], []
get_weather_data(filename, dates, date_index=0, ele_index=16)
ax3.plot(dates, insp_elements, c='blue', alpha=0.7, linewidth=3)
# Format plot.
title = "Maximum Wind Speed in Sit per year"
ax3.set_title(title, fontsize=14)
ax3.set_xlabel('', fontsize=10)
fig.autofmt_xdate()
ax3.set_ylabel("Wind Speed in Mph", fontsize=10)
ax3.tick_params(axis='y', which='minor', labelsize=10)

plt.show()
