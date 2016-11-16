#! /home/ubuntu/anaconda3/bin/python

import os
import pandas as pd

weather_dir = "/home/ubuntu/weatherData/"

i = 1
for file in os.listdir(weather_dir):
    
    timestamp = file.replace("weather_","").replace(".txt","")
    year = int(timestamp[0:4])
    month = int(timestamp[4:6])
    day = int(timestamp[6:8])
    hour = int(timestamp[8:10])
    minute =  int(timestamp[10:12])

    with open(weather_dir + file,"r") as f:
    
        weather_currently = eval(f.read())
    
        if i == 1:
            cols = ['TS_year','TS_month','TS_day','TS_hour','TS_minute']
            for key, value in weather_currently.items():
                cols.append(key)
            weather_df = pd.DataFrame(columns=cols)

        row = [year,month,day,hour,minute]
        for col in cols:
            if "TS_" not in col:
                try:
                    row.append(weather_currently[col])		
                except KeyError:
                    row.append("No Data")
        weather_df.loc[i] = row          
        i = i + 1

weather_df.to_csv("/home/ubuntu/weatherTable/weather.csv",index=False)
