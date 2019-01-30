#functions for database management
#D. Storelli
#9 January 2019

import os
#import sys
#import numpy as np
import pandas as pd

def check_file_system():
    customer_list_copy = pd.read_csv('./master_customer_list.csv')
    paths = customer_list_copy[['financial_records_path','usage_data_path']]
    customer_list_copy['exists'] = paths.apply(check_customer_file_path,axis=1)
    paths = customer_list_copy[['financial_records_path','usage_data_path','exists']]
    paths.apply(create_missing_file_paths,axis=1)
    #print(customer_list_copy)


    return

def check_customer_file_path(series):
    path_financial = series[0]
    path_usage = series[1]
    flag1 = os.path.exists(path_financial)
    flag2 = os.path.exists(path_usage)
    return (flag1,flag2)

def create_missing_file_paths(series):
    path_financial = series[0]
    path_usage = series[1]
    exists_flags = series[2]
    if not exists_flags[0]:
        os.makedirs(path_financial)
    if not exists_flags[1]:
        os.makedirs(path_usage)

def add_new_customer(customer_df):
    with open('master_customer_list.csv', 'a') as f:
        customer_df.to_csv(f, header=False, index=False)
    return

def main():
    #print('test')
    #print(os.path.exists('./customers/'))
    #customer_no	name	address	phone_no	payment_method	account_balance	account_start_date	financial_records_path	usage_data_path

    d = {'customer_no': [10000004],
    'name': ['jack frost'],
    'address': ['13 north pole drive'],
    'phone_no': ['1(555)983-4456'],
    'payment_method':['PayPal'],
    'account_balance': [0],
    'account_start_date': ['1/25/2020'],
    'financial_records_path': ['./customers/10000004/financial/'],
    'usage_data_path': ['./customers/10000004/uasge_data/']}
    new_customer = pd.DataFrame(data=d)
    #add_new_customer(new_customer)
    #check_file_system()

    return

if __name__ == '__main__':
    main()
