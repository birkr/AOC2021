import pandas as pd
import os 
import numpy as np

path, filename = os.path.split(os.path.realpath(__file__))

data = pd.read_csv(path + '/input.txt', delimiter=",", skiprows=0, error_bad_lines=False, header=None, squeeze=True).T

#1st
array = data[0].to_numpy()
column_names = ["position", "total_fuel"]
df = pd.DataFrame(columns = column_names)
for i in range(min(array), max(array)):
    df = df.append({"position":i, "total_fuel":0}, ignore_index=True)
    df.loc[i,'total_fuel'] += sum(abs(array-i))

df[df.total_fuel==df.total_fuel.min()]

#2nd
array = data[0].to_numpy()
column_names = ["position", "total_fuel"]
df = pd.DataFrame(columns = column_names)
for i in range(min(array), max(array)):
    df = df.append({"position":i, "total_fuel":0}, ignore_index=True)
    abs_diff = abs(array-i)
    df.loc[i,'total_fuel'] += sum((abs_diff**2+abs_diff)/2)

df[df.total_fuel==df.total_fuel.min()]
