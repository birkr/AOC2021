import pandas as pd
import os 
import numpy as np

path, filename = os.path.split(os.path.realpath(__file__))

#First
gamma=''
epsilon=''
data = pd.read_csv(path + '/input.txt', sep=" ", header=None, dtype={0:str})
for i in range(len(data.loc[0,0])):
    bit_gamma = data[0].astype(str).str[i].astype(int).value_counts().idxmax()
    bit_eps = data[0].astype(str).str[i].astype(int).value_counts().idxmin()
    gamma = gamma + str(bit_gamma)
    epsilon = epsilon + str(bit_eps)

power_consumption = int(epsilon, 2)*int(gamma, 2)


#Second
oxygen = data
co2 = data
save_d = dict()
save_d1 = dict()
for i in range(len(data.loc[0,0])):
    save_d[i] = oxygen[0].astype(str).str[i].astype(int).value_counts()
    save_d1[i] = co2[0].astype(str).str[i].astype(int).value_counts()
    oxygen = oxygen[oxygen[0].astype(str).str[i].astype(int)==oxygen[0].astype(str).str[i].astype(int).value_counts().idxmax()]
    if len(co2)>1:
        if co2[0].astype(str).str[i].astype(int).value_counts().idxmax()==1:
            co2 = co2[co2[0].astype(str).str[i].astype(int)==0]
        else:
            co2 = co2[co2[0].astype(str).str[i].astype(int)==1]
life_support = power_consumption = int(oxygen.iloc[0,0], 2)*int(co2.iloc[0,0], 2)
