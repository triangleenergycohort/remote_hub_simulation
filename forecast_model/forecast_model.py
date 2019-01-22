# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:20:00 2019

@author: dvsto
"""

import pandas as pd
from battery_soc_model import soc_calc
from battery_soc_model import plot_profiles_month
from datetime import datetime


calendar = pd.read_excel('load model monthly calendar.xlsx',sheet_name=2)
low_on_peak = pd.read_excel('profiles.xlsx',sheet_name='load_low_on_peak')
low_off_peak = pd.read_excel('profiles.xlsx',sheet_name='load_low_off_peak')
med_on_peak = pd.read_excel('profiles.xlsx',sheet_name='load_med_on_peak')
med_off_peak = pd.read_excel('profiles.xlsx',sheet_name='load_med_off_peak')
high_on_peak = pd.read_excel('profiles.xlsx',sheet_name='load_high_on_peak')
high_off_peak = pd.read_excel('profiles.xlsx',sheet_name='load_high_off_peak')

f_gen_profile = pd.read_excel('profiles.xlsx',sheet_name='generation')
solcast_gen_profile = pd.read_csv('./weather data/locations/curtailment scenario/gen_profile.csv')


#aggregate monthly load data
load = pd.DataFrame([])
#gen = pd.DataFrame([])

for d in calendar.load_profile:
    daily_load_profile = globals()[d]
    load = pd.concat([load,daily_load_profile],ignore_index=True)
    #daily_gen_profile = f_gen_profile
    #gen = pd.concat([gen,daily_gen_profile],ignore_index=True)
    
    
#extract and synchronize timestamps
delta_t = 0.5
solcast_first_endtime = datetime.strptime(solcast_gen_profile.loc[(len(solcast_gen_profile.time)-1),'period_end'],'%Y-%m-%dT%H:%M:00.0000000Z')
#load timestamp needs to be verified
load_first_endtime = datetime(2019,1,12,21)
time_sync_delta = solcast_first_endtime - load_first_endtime
offset_index = int((time_sync_delta.days*24+time_sync_delta.seconds/3600)/delta_t)

load = load[offset_index:].reset_index()
t_month = pd.Series(range(len(load.ld_energy)))
t_month = t_month*delta_t
load['t_month'] = t_month
#gen['t_month'] = t_month
#print(len(t_month))

#calculate and plot results
soc_week = soc_calc(load,solcast_gen_profile)
plot_profiles_month(load[:len(solcast_gen_profile.time)],solcast_gen_profile,soc_week)    

#find curtailment points


