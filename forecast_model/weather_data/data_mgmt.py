# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:55:47 2019

@author: dvsto
"""

import pandas as pd

#calculate electricity generation
def gen_calc(irradiance):
    #constants
    pannel_size = 0.42240
    eff = 0.145
    derate = 0.0
    return irradiance*pannel_size*eff*(1-derate)

#create generation csv file from irradiance
def new_file_mgmt(path,filename):
    irradiance = pd.read_csv(path+filename)
    irradiance = irradiance.rename(columns={'Unnamed: 0': 'index'})
    
    #calculate time series
    if irradiance.loc[0,'period'] == 'PT30M':
        delta_t = 0.5
    irradiance['time'] = irradiance.index*delta_t

    irradiance['gen_energy'] = irradiance.ghi.apply(gen_calc)
    
    #plot results
    irradiance.plot(x='index',y='gen_energy')
    
    output = irradiance[['time','gen_energy','period_end']]
    output.to_csv(path+'gen_profile.csv')
    return


#calculate insolation
def insolation_calc(df):
    #add eq to determine delta t
    s=0
    delta_t = df.time[1]-df.time[0]
    for x in range(len(df.gen_energy)):
        s = s+df.gen_energy[x]*delta_t
    return s

p = './locations/loc02/'
f = 'data.csv'
new_file_mgmt(p,f)
