#functions for database management
#D. Storelli
#9 January 2019

import os
#import sys
#import numpy as np
import pandas as pd

def check_file_system():
    customer_list_copy = pd.read_excel('./master_customer_list.xlsx')
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

def main():
    #print('test')
    #print(os.path.exists('./customers/'))
    check_file_system()

    return

if __name__ == '__main__':
    main()
