#script to check forecast for loadshift scenario

import pandas as pd
import matplotlib.pyplot as plt
import csv
from forecast_model.battery_soc_model import soc_calc
from forecast_model.forecast_model import identify_loadshift

def main():
    path = './forecast_model/weather_data/locations/curtailment scenario/gen_profile.csv'
    gen_forecast = pd.read_csv(path)
    l = identify_loadshift(gen_forecast)
    print('loadshift recommended \ntimestamps:\n',l)
    plot_forecast_with_loadshift(path,l)
    return

def plot_forecast_with_loadshift(path,list):
    #font = {'fontname':'Arial'}
    #(0.75,0.75,1)
    fig = plt.figure()
    fig.patch.set_facecolor('0.5')
    x = []
    y1 = []
    y2 = []
    y3 = []

    with open(path,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots,None)
        for row in plots:
            x.append(float(row[1]))
            y1.append(float(row[2]))
            #y2.append(float(row[3]))
            #y3.append(float(row[4]))

    plt.plot(x,y1, label='SHS Generation')
    #plt.plot(x,y2, label='', color='0.6')
    #plt.plot(x,y3, label='',color='0.6')
    #plt.fill_between(x,y1,y2,facecolor='0.65')
    #plt.fill_between(x,y1,y3,facecolor='0.65')
    plt.xlabel('time (hours)') #to change font add **font
    plt.ylabel('watts')
    plt.title('Week Ahead Forecast')
    plt.legend()

    for item in list:
        plt.arrow(item[0],0,-5,-5)

    plt.show(fig)
    return

if __name__ == '__main__':
    main()
