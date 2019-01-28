#script to view maintenance database

import csv

print('Active Maintenance Requests:')
print('| customer_no | name | repair_category | date_of_request |')
with open('./customer_database/maintenance_queue/maintenance_queue_data.csv', encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    #print(reader['customer_no'])
    for row in reader:
        print('| '+row['customer_no']+' | '+row['name']+' | '+row['repair_category']+' | '+row['date_of_request']+' |')
