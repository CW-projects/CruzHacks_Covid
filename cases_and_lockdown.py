from urllib.request import urlretrieve as retrieve
import matplotlib.pyplot as plt
import csv

# looks like you are using a static download, but the API has changed.. using legacy will temporarily make the url work..
# url = "https://legacy.healthdata.gov/node/3736471/download"
# retrieve(url, "weekly_death_causes.csv")
states_csv = open("weekly_death_causes.csv", "rt")
rdr = csv.reader(states_csv)

def state_cases_lockdowns(state):
    weeks = list(range(52))
    diabetes = list()
    natural = list()
    covid = list()
    covid_only = list()
    alz = list()
    cancer = list()
    first = True
    for row in rdr:
        if first:
            print(row)
            first = False
        if row[0] == state and row[1] == "2020":
            print(row)
            print(row[19])
            covid_only.append(int(row[19])) if row[19] != '' else covid_only.append(0)
            cancer.append(int(row[7])) if row[7] != '' else cancer.append(0)
            covid.append(int(row[18])) if row[18] != '' else covid.append(0)
            covid[-1] += int(row[19]) if row[19] != '' else 0
            diabetes.append(int(row[8])) if row[8] != '' else diabetes.append(0)
            natural.append(int(row[6])) if row[6] != '' else natural.append(0)
            alz.append(int(row[9])) if row[9] != '' else alz.append(0)
        if len(diabetes) >= len(weeks):
            break
    plt.plot(weeks, covid, label="Covid Related")
    # plt.plot(weeks, covid_only, label="Covid ONLY")
    plt.plot(weeks, cancer, label="Cancer")
    plt.plot(weeks, diabetes, label="Diabetes")
    plt.plot(weeks, natural, label="Natural")
    plt.plot(weeks, alz, label="Alzheimers")

    plt.legend()
    plt.show()





if __name__ == "__main__":
    state_cases_lockdowns('Arizona')
