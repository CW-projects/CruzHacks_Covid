from urllib.request import urlretrieve as retrieve
import matplotlib.pyplot as plt
import csv
# RETRIEVE THE DOCUMENTS
url_death_counts = 'https://data.cdc.gov/api/views/3apk-4u4f/rows.csv?accessType=DOWNLOAD'


retrieve(url_death_counts, 'total_age_deaths.csv')

# rt = "read" and "text" mode
death_counts = open('total_age_deaths.csv', 'rt')

x = 0
dths_by_age = list()
des_grps = ["0-17 years", "18-29 years", "30-49 years", "50-64 years", "65-74 years", "75-84 years", "85 years and over"]
first = True
age = 0
for row in death_counts:
    if first:
        first = False
        continue
    split_row = row.split(',')
    if(split_row[3] == 'Male'):
        dths_by_age.append(int(split_row[6]))
    else:
        dths_by_age[age] += int(split_row[6])
        age += 1
    print(f"Row: {split_row}")


print(dths_by_age)
dths_by_age.pop(-1)
plt.xlabel("Age in Years (0-84)")
plt.ylabel("Number of Deaths attributed to COVID-19")
plt.title("COVID-19 Deaths as a Funtion of Age")

ages_axes = list(range(85))
plt.bar(ages_axes, dths_by_age)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(ages_axes, dths_by_age)

plt.show()