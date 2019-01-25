#script to download recent forecast and display in matplotlib window

import matplotlib.pyplot as plt
import csv


def matplot_forecast(path):
    x = []
    y = []

    with open(path,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots,None)
        for row in plots:
            x.append(float(row[1]))
            y.append(float(row[2]))

    plt.plot(x,y, label='SHS Generation')
    plt.xlabel('time (hours)')
    plt.ylabel('watts')
    plt.title('Week Ahead Forecast')
    plt.legend()
    plt.show()
    return

def main():
    matplot_forecast('./forecast_model/weather_data/locations/loc02/gen_profile.csv')

if __name__ == '__main__':
    main()
