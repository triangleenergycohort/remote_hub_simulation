#script to download recent forecast and display in matplotlib window

import matplotlib.pyplot as plt
import csv


def matplot_forecast(path):
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
            y2.append(float(row[3]))
            y3.append(float(row[4]))

    plt.plot(x,y1, label='SHS Generation')
    plt.plot(x,y2, label='', color='0.6')
    plt.plot(x,y3, label='',color='0.6')
    plt.fill_between(x,y1,y2,facecolor='0.65')
    plt.fill_between(x,y1,y3,facecolor='0.65')
    plt.xlabel('time (hours)') #to change font add **font
    plt.ylabel('watts')
    plt.title('Week Ahead Forecast')
    plt.legend()
    plt.show(fig)
    return

def main():
    matplot_forecast('./forecast_model/weather_data/locations/loc02/gen_profile.csv')

if __name__ == '__main__':
    main()
