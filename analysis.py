import pandas as pd
import matplotlib

dsales = pd.read_csv("data/salesdaily.csv") #daily sales
hsales = pd.read_csv("data/saleshourly.csv") #hourly
msales = pd.read_csv("data/salesmonthly.csv") #monthly
wsales = pd.read_csv("data/salesweekly.csv") #weekly

#print(dsales.head()) #testing if read-in works

# TOTAL SALES QUANT FOR EACH DRUG
msales_clean = msales.drop("datum", axis = 1)   #looking at total, so agg monthly

print(sum(msales_clean["M01AB"]))

#print(msales_clean["M01AB"])

for i in msales_clean:
    print("Drug Name:", f'{i}|||', "Total:", f'{sum(msales_clean[i]):.2f}')