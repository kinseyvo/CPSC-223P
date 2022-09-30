import csv
from datetime import date, datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rainfalls = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rainfall = float(row[3])
        dates.append(current_date)
        rainfalls.append(rainfall)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, c='blue')

title = "Daily rainfall amounts - 2018\nSitka"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
