# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:55:47 2019

@author: dvsto
"""

import pandas as pd

irradiance = pd.read_csv('./locations/loc01/data.csv')
irradiance = irradiance.rename(columns={'Unnamed: 0': 'index'})

#extract timestamp
#** add function to extract and synchronize timestamps **

#calculate electricity generation
def gen_calc(irradiance):
    #constants
    pannel_size = 0.42240
    eff = 0.145
    return irradiance*pannel_size*eff

irradiance['generation_watts'] = irradiance.ghi.apply(gen_calc)

#plot results
irradiance.plot(x='index',y='generation_watts')