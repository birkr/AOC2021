import pandas as pd
import os 
import numpy as np

path, filename = os.path.split(os.path.realpath(__file__))

data = pd.read_csv(path + '/input.txt', sep=" -> ", skiprows=0, error_bad_lines=False, header=None)
data[['x1','y1']] = data[0].str.split(",", expand=True)
data[['x2','y2']] = data[1].str.split(",", expand=True)
data = data[['x1', 'y1', 'x2','y2']].apply(pd.to_numeric, errors='coerce')

#1st
df = pd.DataFrame(np.random.random((1000, 1000)))
for col in df.columns:
    df[col].values[:] = 0
    
for index, row in data.iterrows():
    if row.x1 == row.x2:
       df.iloc[min(row.y1,row.y2):(max(row.y1,row.y2)+1), row.x1] += 1
    if row.y1 == row.y2:
       df.iloc[row.y1, min(row.x1,row.x2):(max(row.x1,row.x2)+1)] += 1

(df.values >= 2).sum()

#2nd
df = pd.DataFrame(np.random.random((1000, 1000)))
for col in df.columns:
    df[col].values[:] = 0
    
for index, row in data.iterrows():
    if row.x1 == row.x2:
       df.iloc[min(row.y1,row.y2):(max(row.y1,row.y2)+1), row.x1] += 1
    if row.y1 == row.y2:
       df.iloc[row.y1, min(row.x1,row.x2):(max(row.x1,row.x2)+1)] += 1
    if abs(row.x1-row.x2)==abs(row.y1-row.y2):
        for i in range(abs(row.x1-row.x2)+1):
            if (row.x1>row.x2 and row.y1>row.y2) or (row.x1<row.x2 and row.y1<row.y2):
                df.iloc[min(row.y1,row.y2)+i,min(row.x1,row.x2)+i] += 1
            else:
                df.iloc[max(row.y1,row.y2)-i,min(row.x1,row.x2)+i] += 1
(df.values >= 2).sum()
