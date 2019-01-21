# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:55:47 2019

@author: dvsto
"""

import pandas as pd

irradiance = pd.read_csv('./locations/loc01/data.csv')
irradiance = irradiance.rename(columns={'Unnamed: 0': 'index'})

#calculate time series
if irradiance.loc[0,'period'] == 'PT30M':
    delta_t = 0.5
irradiance['time'] = irradiance.index*delta_t

#calculate electricity generation
def gen_calc(irradiance):
    #constants
    pannel_size = 0.42240
    eff = 0.145
    derate = 0.0
    return irradiance*pannel_size*eff*(1-derate)

irradiance['gen_energy'] = irradiance.ghi.apply(gen_calc)

#plot results
#irradiance.plot(x='index',y='generation_watts')

output = irradiance[['time','gen_energy','period_end']]
output.to_csv('./locations/loc01/gen_profile.csv')