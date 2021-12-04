import pandas as pd
import os 
path, filename = os.path.split(os.path.realpath(__file__))

#First
data = pd.read_csv(path + '/input.txt', sep=" ", header=None)
data['lag'] = data[0].shift(1)
data.dropna()
increases = sum(data[0]>data['lag'])


#Second
data = pd.read_csv(path + '/input.txt', sep=" ", header=None)
data['Rolling_sum'] = data[0].rolling(3).sum()
data.dropna()
data['lag_rolling'] = data['Rolling_sum'].shift(1)
increases_rolling = sum(data['Rolling_sum']>data['lag_rolling'])
