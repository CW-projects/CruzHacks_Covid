from urllib.request import urlretrieve as retrieve
import matplotlib.pyplot as plt
import csv
# RETRIEVE THE DOCUMENTS
# url_death_counts = 'https://data.cdc.gov/api/views/9bhg-hcku/rows.csv?accessType=DOWNLOAD'
# url_lockdown_policies = 'https://healthdata.gov/sites/default/files/state_policy_updates_20210114_1920.csv'
#
# retrieve(url_death_counts, 'age_sex_state.csv')
# retrieve(url_lockdown_policies, 'lockdowns.csv')

# rt = "read" and "text" mode
death_counts = open('age_sex_state.csv', 'rt')

x = 0
dths_by_age = list()
des_grps = ["0-17 years", "18-29 years", "30-49 years", "50-64 years", "65-74 years","75-84 years", "85 years and over"]

for row in death_counts:
    split_row = row.split(',')
    if (split_row[5] in des_grps):
        print(f"Row: {row}")
        print(f"Split: {split_row}")
        dths_by_age.append(int(split_row[6]))
    x+=1
    if (len(dths_by_age) >= len(des_grps)):
        break
print(dths_by_age)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(des_grps, dths_by_age)
plt.show()

