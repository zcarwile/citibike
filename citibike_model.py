#! /Users/zcarwile/anaconda/envs/anaconda34/bin/python

import subprocess

# coding: utf-8

# In[1]:

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz


# In[2]:

df = pd.read_csv('features.csv')
df.head(5)


# In[3]:

df['empty'] = df['availableBikes'] == 0
df['full'] = df['availableDocks'] == 0
#df[df['empty'] == True]

try:
    df = df.drop('TS_day',1)
except:
    pass

df.head(5)


# In[4]:

def encode_feature(df, old_column, new_column):
 
    df_mod = df.copy()
    targets = df_mod[old_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod[new_column] = df_mod[old_column].replace(map_to_int)

    return df_mod


# In[5]:

df = encode_feature(df,'icon','icon_enum')
df.tail()


# In[6]:

# Targets are "empty" and "full" (2 separate classifiers OK)

features = ['TS_hour','temperature','weekday','icon_enum']

X = df[features]
y = df['empty']
X = X.dropna(axis=1)

dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)

dt.fit(X, y)


# In[9]:

with open("dt.dot", 'w') as f:
    export_graphviz(dt, out_file=f,
                    feature_names=features)

command = ["dot", "-Tsvg", "dt.dot", "-o", "dt.svg"]
subprocess.check_call(command)


# In[8]:



