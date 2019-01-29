# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:20:00 2019

@author: dvsto
"""

import pandas as pd
#from battery_soc_model import soc_calc
#from battery_soc_model import plot_profiles
from datetime import datetime

def load_model():
    calendar = pd.read_excel('load model monthly calendar.xlsx',sheet_name=2)
    low_on_peak = pd.read_excel('profiles.xlsx',sheet_name='load_low_on_peak')
    low_off_peak = pd.read_excel('profiles.xlsx',sheet_name='load_low_off_peak')
    med_on_peak = pd.read_excel('profiles.xlsx',sheet_name='load_med_on_peak')
    med_off_peak = pd.read_excel('profiles.xlsx',sheet_name='load_med_off_peak')
    high_on_peak = pd.read_excel('profiles.xlsx',sheet_name='load_high_on_peak')
    high_off_peak = pd.read_excel('profiles.xlsx',sheet_name='load_high_off_peak')
    
    f_gen_profile = pd.read_excel('profiles.xlsx',sheet_name='generation')
    solcast_gen_profile = pd.read_csv('./weather_data/locations/loc02/gen_profile.csv')
    
    
    #aggregate monthly load data
    load = pd.DataFrame([])
    #gen = pd.DataFrame([])
    
    for d in calendar.load_profile:
        daily_load_profile = locals()[d]
        load = pd.concat([load,daily_load_profile],ignore_index=True)
        #daily_gen_profile = f_gen_profile
        #gen = pd.concat([gen,daily_gen_profile],ignore_index=True)
    
    
    #extract and synchronize timestamps
    delta_t = 0.5
    solcast_first_endtime = datetime.strptime(solcast_gen_profile.loc[(len(solcast_gen_profile.time)-1),'period_end'],'%Y-%m-%dT%H:%M:00.0000000Z')
    #load timestamp needs to be verified
    load_first_endtime = datetime(2019,1,12,15)
    time_sync_delta = solcast_first_endtime - load_first_endtime
    offset_index = int((time_sync_delta.days*24+time_sync_delta.seconds/3600)/delta_t)
    
    load = load[offset_index:].reset_index()
    t_month = pd.Series(range(len(load.ld_energy)))
    t_month = t_month*delta_t
    load['t_month'] = t_month
    #gen['t_month'] = t_month
    #print(len(t_month))
    
    #'''
    #calculate and plot results
    soc_week = soc_calc(load,solcast_gen_profile)
    plot_profiles(load[:len(solcast_gen_profile.time)],solcast_gen_profile,soc_week)
    #'''
    return


#calculate insolation
def insolation_calc(df):
    #add eq to determine delta t
    s=0
    delta_t = df.time[1]-df.time[0]
    for x in range(len(df.gen_energy)):
        s = s+df.gen_energy[x]*delta_t
    return s

#find loadshift points
def identify_loadshift(gen_df):
    #init
    delta_t = gen_df.time[1]-gen_df.time[0]
    threshold = 120
    t = 0
    offset = int(24/delta_t)
    low_pv_count = 0
    timestamps = []
    loadshift_flag = False

    while (t)<len(gen_df.gen_energy):
        if (t+offset)>len(gen_df.gen_energy):
            offset = len(gen_df.gen_energy)-t
        else:
            offset = int(24/delta_t)

        i = insolation_calc(gen_df[t:t+offset].reset_index())
        #print(i)
        if i<threshold:
            #print('low insolation detected')
            timestamps.append((gen_df.time[t],gen_df.period_end[t]))
            low_pv_count = low_pv_count+1
            if low_pv_count >= 2:
                loadshift_flag = True
        else:
            low_pv_count=0
        t = t+offset

    if loadshift_flag:
        #print('need loadshift')
        #print(timestamps)
        return timestamps
    else:
        return

#send loadshift report to device
def send_loadshift_report(customer,times,dod_increment):
    email_text = 'Loadshift recommended'+'\n'
    email_text = email_text+'Start time: '+times[0]+'\n'+'End time: '+times[1]+'\n'
    email_text = email_text+'Max daily incremental DOD: '+dod_increment
    print(email_text)

    return


def main():
    solcast_gen_profile = pd.read_csv('./weather_data/locations/loc02/gen_profile.csv')
    times = identify_loadshift(solcast_gen_profile)
    if times:
        send_loadshift_report('10000001',times,'20%')
        
    load_model()
    return

if __name__ == '__main__':
    main()

