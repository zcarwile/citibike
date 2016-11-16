#! /Users/zcarwile/anaconda/envs/anaconda34/bin/python

import pandas as pd
import json
import sys
import os

stationDataDir = "/Users/zcarwile/Documents/content/sales_engineering_demos/citibike/bikeJSON/"
stationDataDirOut = "/Users/zcarwile/Documents/content/sales_engineering_demos/citibike/bikeCSV/"

for fname in os.listdir(stationDataDir):

    try:
        with open(stationDataDir + fname,'r') as f:
            s  = json.loads(f.read())
            station_json = s['stationBeanList']
            station_df = pd.DataFrame(station_json)
            fname_csv = fname.replace(".json",".csv")
            station_df.to_csv(stationDataDirOut + fname_csv, index=False)
    except:
        print("Error converting file: " + fname)
        continue
