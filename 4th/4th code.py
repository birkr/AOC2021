import pandas as pd
import os 
import numpy as np

path, filename = os.path.split(os.path.realpath(__file__))

data = pd.read_csv(path + '/input.txt', sep=r"\s+", skiprows=1, error_bad_lines=False, header=None)
data_numbers = pd.read_csv(path + '/input.txt', sep=",",  nrows=1, header=None)

data_coins = data.copy()
for i in np.nditer(data_numbers.values):
    data_coins[data_coins == int(i)] = 0
    if data_coins.sum(axis=1).min()==0:
        index = data_coins.sum(axis=1).idxmin()
        index_start = int((index)/5)*5
        index_end = index_start+5
        break

final_score = sum(data_coins.iloc[index_start:index_end].sum())*i

#second
breaking = 0
data_coins = data.copy()
for i in np.nditer(data_numbers.values):
    data_coins[data_coins == int(i)] = 0
    for j in data_coins.index[::5]:
        if (any(data_coins.loc[j:j+5].sum(axis=1)==0)) | (any(data_coins.loc[j:j+5].sum(axis=0)==0)):
            if len(data_coins)==5:
                breaking = 1
                break
            data_coins = data_coins[~data_coins.index.isin(range(j,j+5))]
    if breaking == 1:
        break
    
final_score1 = sum(data_coins.sum())*i

