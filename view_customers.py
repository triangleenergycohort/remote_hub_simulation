#script to view customer database

import csv

print('Master Customer List:')
print('| customer_no | name | account_balance |')
with open('./customer_database/master_customer_list.csv', encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    #print(reader['customer_no'])
    for row in reader:
        print('| '+row['customer_no']+' | '+row['name']+' | '+row['account_balance']+' |')
