def get_temp_indices(header_row):
    """Accepts header_row and returns a tuple containing indices of high and low temperatures"""

    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')

    indices_tuple = (high_index, low_index)

    return indices_tuple


import csv
from datetime import datetime
from os import name 

import matplotlib.pyplot as plt

filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    name_index = header_row.index('NAME')
    index = get_temp_indices(header_row)
    high_index = int(index[0]) 
    low_index = int(index[1])

    print(f'The row index containing high temperatures is {high_index}.')
    print(f'The row index containing low temperatures is {low_index}.\n')

    # Get dates, and high and low temperatures from the file
    dates, highs, lows = [], [], [] 
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

        try:
            high = int(row[index[0]])
            low = int(row[index[1]])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

print(f'\nThe highest temperature in {row[name_index]} is {max(highs)}.')
print(f'The lowest temperature in {row[name_index]} is {min(lows)}.\n')

# Plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


# Format plot
title = f"Daily high and low temperatures - 2018\n{row[name_index]}"
ax.set_title(title, fontsize=20)

ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() 
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)


#Display 10 degrees above the highest max and 10 degrees below the lowest minimum temperature
highest_max = max(highs)
lowest_min = min(lows)
plt.ylim(lowest_min - 10, highest_max + 10)

plt.show()