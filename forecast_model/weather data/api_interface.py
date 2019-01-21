#Interface for Solcast API

import requests
import json
import csv
import pandas as pd

def get_solcast_insolation():
    success = False
    r = requests.get("https://api.solcast.com.au/radiation/estimated_actuals?longitude=120.78&latitude=-8.60&api_key=xPd9I0BI0abRZSCt8kiDisjEvFQIF7bT&format=json")
    print(r.status_code)

    if r.status_code == 200:
        success = True
        data = r.json()
        data = data['estimated_actuals']
        #print(data['estimated_actuals'])
        #save to json file
        #'''
        #** add logic to determine storage location **
        filedir = './locations/loc01/'
        with open(filedir+'data.json', 'w') as outfile:
            json.dump(data, outfile)
        #'''
        #convert to csv
        df = pd.read_json(filedir+'data.json')
        #print(df.head())
        df.to_csv(filedir+'data.csv')

    return success

def main():
    s = get_solcast_insolation()
    print('Data retrieved: '+str(s))

if __name__ == '__main__':
    main()
