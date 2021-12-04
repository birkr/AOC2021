import pandas as pd
import os 
import numpy as np

path, filename = os.path.split(os.path.realpath(__file__))

#First
data = pd.read_csv(path + '/input.txt', sep=" ", header=None)
data_group = data.groupby(by=0).sum()
horizontal = data_group.loc['forward'].values
depth = data_group.loc['down'].values - data_group.loc['up'].values
position = horizontal*depth

#second
data = pd.read_csv(path + '/input.txt', sep=" ", header=None)
data['aim'] = np.nan
data['depth'] = np.nan
data['horizontal'] = np.nan

for index, row in data.iterrows():
    if index==0:
        if data.loc[index,0]=='down':
            data.loc[index,'aim'] = data.loc[index,1]
        if data.loc[index,0]=='up':
            data.loc[index,'aim'] = -data.loc[index,1]
        if data.loc[index,0]=='forward':
            data.loc[index,'aim'] = 0
            data.loc[index,'depth'] = 0
            data.loc[index,'horizontal'] = data.loc[index,1]
    elif data.loc[index,0]=='down':
        data.loc[index,'aim']=data.loc[index-1,'aim']+data.loc[index,1]
    elif data.loc[index,0]=='up':
        data.loc[index,'aim']=data.loc[index-1,'aim']-data.loc[index,1]
    elif data.loc[index,0]=='forward':
        data.loc[index,'aim'] = data.loc[index-1,'aim']
        data.loc[index,'depth'] = data.loc[index,'aim']*data.loc[index,1]
        data.loc[index,'horizontal'] = data.loc[index,1]
        
position = data.sum(axis=0,numeric_only=True)
end_pos = position['depth']*position['horizontal']
