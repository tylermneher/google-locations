

import json
f = open('Records.json')
data = json.load(f)

locat = []

for i in data['locations']:
	locat.append(i)

f.close()

print(locat[0])

print(len(locat[0]))


for i in locat:
	if len(i) == 6:
		pass
	else:
		i["source"] = "NaN"

