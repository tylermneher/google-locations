import json
import pandas as pd

f = open('Records.json')
data = json.load(f)

locat = []

for i in data['locations']:
	locat.append(i)

f.close()

print(locat[0])

print(len(locat[0]))


df = pd.DataFrame.from_dict(locat)
print(df.columns)
print(df)

df.to_csv('Records.csv')
