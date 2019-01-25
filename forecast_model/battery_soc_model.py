# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 13:09:55 2018

@author: dvsto
"""
import pandas as pd
import matplotlib.pyplot as plt

def soc_calc(load_profile,gen_profile):
    #battery configuration
    battery_voltage = 12
    battery_capacity = 20 #Ah
    #model parameters
    deltat = 0.5
    initial_soc = 0.9
    SOC = pd.Series([initial_soc]*len(gen_profile))    
    #calculation
    for t in range(0,(len(SOC)-1)):
        I = (gen_profile.gen_energy[t+1]-load_profile.ld_energy[t+1])/battery_voltage
        delta_SOC = I*deltat/battery_capacity
        
        if (SOC[t]+delta_SOC)>1:
            SOC[t+1] = 1
        elif (SOC[t]+delta_SOC)<0:
            SOC[t+1] = 0
        else:
            SOC[t+1] = SOC[t]+delta_SOC
        
    #print(SOC.head(48))
    return SOC

def plot_profiles(load_profile,gen_profile,soc_profile):
    #for file output use figsize=[16,9]
    fig, ax1 = plt.subplots()
    
    color = 'tab:red'
    ax1.set_xlabel('time (hr)')
    ax1.set_ylabel('Watts', color=color)
    ax1.plot(gen_profile.time, gen_profile.gen_energy, color=color)
    ax1.plot(load_profile.t_month, load_profile.ld_energy, '--', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    
    color = 'tab:blue'
    ax2.set_ylabel('SOC', color=color)  # we already handled the x-label with ax1
    ax2.plot(load_profile.t_month, soc_profile, color=color)
    ax2.set_ylim([0,1])
    ax2.tick_params(axis='y', labelcolor=color)
    
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
    return

'''
#read from csv files
f_load_profile = pd.read_excel('profiles.xlsx',sheet_name='load_low_off_peak')
f_gen_profile = pd.read_excel('profiles.xlsx',sheet_name='generation')

f_soc = soc_calc(f_load_profile,f_gen_profile)
#plot_profiles(f_load_profile,f_gen_profile,f_soc)
'''
