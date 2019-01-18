#Interface for Solcast API

import requests
import json
import csv
import pandas as pd

r = requests.get("https://api.solcast.com.au/radiation/estimated_actuals?longitude=120.78&latitude=-8.60&api_key=xPd9I0BI0abRZSCt8kiDisjEvFQIF7bT&format=json")
#https://api.solcast.com.au/radiation/estimated_actuals?longitude=120.78&latitude=-8.60&api_key=xPd9I0BI0abRZSCt8kiDisjEvFQIF7bT
print(r.status_code)

#if response.status_code == 200:
data = r.json()
#print(data)
#save to json file
'''
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
'''
#convert to csv
'''
f = csv.writer(open("test.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
#f.writerow(["ghi", "ebh", "dni", "dhi", "cloud_opacity", "period_end", "period"])
x=r
for x in x:
    f.writerow([x["ghi"],
                x["ebh"],
                x["dni"],
                x["dhi"]["name"],
                x["cloud_opacity"],
                x["period_end"],
                x["period"]])
#'''




df = pd.read_json('data.json')
#print(df.head())
df.to_csv('data.csv')
