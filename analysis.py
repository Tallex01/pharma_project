import pandas as pd
import matplotlib
import sqlite3

dsales = pd.read_csv("data/salesdaily.csv") #daily sales
hsales = pd.read_csv("data/saleshourly.csv") #hourly
msales = pd.read_csv("data/salesmonthly.csv") #monthly
wsales = pd.read_csv("data/salesweekly.csv") #weekly

#print(dsales.head()) #testing if read-in works

### 1. TOTAL SALES QUANT FOR EACH DRUG
msales_clean = msales.drop("datum", axis = 1)   #looking at total, so agg monthly

print(sum(msales_clean["M01AB"]))

#print(msales_clean["M01AB"])

for i in msales_clean:
    print("Drug Name:", f'{i}', f"\nTotal:", f'${sum(msales_clean[i]):,.2f}\n')

# ^^^displays total sales for each


### 2. Brands w/ highest total sales
highest = []

for i in msales_clean:
    highest.append((i, sum(msales_clean[i])))
highest = sorted(highest, key = lambda tup: tup[1], reverse = True)
print(highest)

# Top 3 total: N02BE, N05B, R03


### 3. Top 3 drug brands Jan 2015, July 2016, Sept 2017
print(hsales)

conn = sqlite3.connect('pharma.db')
cursor = conn.cursor()

hsales.to_sql('hourly', conn, if_exists = 'replace', index = False)

query1 = """
    SELECT 
    SUM(M01AB) as sum1,
    SUM(M01AE) as sum2,
    SUM(N02BA) as sum3,
    SUM(N02BE) as sum4,
    SUM(N05B) as sum5,
    SUM(N05C) as sum6,
    SUM(R03) as sum7,
    SUM(R06) as sum8
    FROM hourly
    WHERE Year = 2015
    AND Month = 1 
    """
query2 = """
    SELECT 
    SUM(M01AB) as sum1,
    SUM(M01AE) as sum2,
    SUM(N02BA) as sum3,
    SUM(N02BE) as sum4,
    SUM(N05B) as sum5,
    SUM(N05C) as sum6,
    SUM(R03) as sum7,
    SUM(R06) as sum8
    FROM hourly
    WHERE Year = 2016
    AND Month = 7 
"""

query3 = """
    SELECT 
    SUM(M01AB) as sum1,
    SUM(M01AE) as sum2,
    SUM(N02BA) as sum3,
    SUM(N02BE) as sum4,
    SUM(N05B) as sum5,
    SUM(N05C) as sum6,
    SUM(R03) as sum7,
    SUM(R06) as sum8
    FROM hourly
    WHERE Year = 2017
    AND Month = 9; 
"""

cursor.execute(query1)
result1 = cursor.fetchall()

cursor.execute(query2)
result2 = cursor.fetchall()

cursor.execute(query3)
result3 = cursor.fetchall()

conn.commit()
conn.close()

print(result1)
print(result2)
print(result3)
# Drugs 4,7, and 3 (N02BE, R03, and N02BA) had the highest sales in Jan 2015
# Drugs 4, 5, and 1 (N02BE, N05B, and M01AB) had the highest sales in July 2016
# Drugs 4, 5, and 7 (N02BE, N05B, and R03) had the highest sales in September 2017



### 4. Most sold drug in 2017
conn = sqlite3.connect('pharma.db')
cursor = conn.cursor()

query1 = """
    SELECT 
    COUNT(M01AB) as count1,
    COUNT(M01AE) as count2,
    COUNT(N02BA) as count3,
    COUNT(N02BE) as count4,
    COUNT(N05B) as count5,
    COUNT(N05C) as count6,
    COUNT(R03) as count7,
    COUNT(R06) as count8
    FROM hourly
    WHERE Year = 2017
    """

cursor.execute(query1)
result1 = cursor.fetchall()

conn.commit()
conn.close()

print(result1)

hdf = pd.DataFrame(hsales)
d1 = len(hdf)
print(d1)

for i in hsales:
    print(i)



### 5. 



### 6. 






