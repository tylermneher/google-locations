

import json
f = open('Records.json')
data = json.load(f)

locat = []

for i in data['locations']:
	locat.append(i)

f.close()

print(locat[0])
