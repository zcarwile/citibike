#! /Users/zcarwile/anaconda/envs/anaconda34/bin/python

import json
from urllib.request import urlopen
import datetime

dir = "/Users/zcarwile/Documents/content/sales_engineering_demos/citibike/"
timestamp = datetime.datetime.strftime(datetime.datetime.now(),"%Y%m%d%H%M%S")

response = urlopen("https://feeds.citibikenyc.com/stations/stations.json")
j = response.read().decode('utf-8')

fname = dir + "citibike_" + timestamp + ".json"
with open(fname,"w") as f:
    f.write(j)

weather_raw = urlopen("https://api.forecast.io/forecast/62b3f08596594954c4856e61610736ee/40.71,-74.01")
weather_json = json.loads(weather_raw.read().decode('utf-8'))
weather_currently = weather_json['currently']
weather = str(weather_currently)

fname = dir + "weather_" + timestamp + ".txt"
with open(fname,"w") as f:
    f.write(weather)
