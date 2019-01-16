# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:20:00 2019

@author: dvsto
"""

import pandas as pd
from battery_soc_model import soc_calc
from battery_soc_model import plot_profiles_month

calendar = pd.read_excel('load model monthly calendar.xlsx',sheet_name=2)
low_on_peak = pd.read_excel('profiles.xlsx',sheet_name='load_low_on_peak')
low_off_peak = pd.read_excel('profiles.xlsx',sheet_name='load_low_off_peak')
med_on_peak = pd.read_excel('profiles.xlsx',sheet_name='load_med_on_peak')
med_off_peak = pd.read_excel('profiles.xlsx',sheet_name='load_med_off_peak')
high_on_peak = pd.read_excel('profiles.xlsx',sheet_name='load_high_on_peak')
high_off_peak = pd.read_excel('profiles.xlsx',sheet_name='load_high_off_peak')
f_gen_profile = pd.read_excel('profiles.xlsx',sheet_name='generation')


load = pd.DataFrame([])
gen = pd.DataFrame([])

for d in calendar.load_profile:
    daily_load_profile = globals()[d]
    load = pd.concat([load,daily_load_profile],ignore_index=True)
    daily_gen_profile = f_gen_profile
    gen = pd.concat([gen,daily_gen_profile],ignore_index=True)
    
t_month = pd.Series(range(len(calendar.day)*len(f_gen_profile.time)))
delta_t = 0.5
t_month = t_month*delta_t
load['t_month'] = t_month
gen['t_month'] = t_month
#print(len(t_month))

soc_month = soc_calc(load,gen)
plot_profiles_month(load,gen,soc_month)    
    
