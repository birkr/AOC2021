import pandas as pd
import os 
import numpy as np

path, filename = os.path.split(os.path.realpath(__file__))

data = pd.read_csv(path + '/input.txt', delimiter=",", skiprows=0, error_bad_lines=False, header=None, squeeze=True).T

list_data = data[0].tolist()

for day in range(80):
    for i in range(len(list_data)):
        if list_data[i]==0:
            list_data[i] = 6
            list_data.append(8)
        else:
            list_data[i] -= 1

len(list_data)


#second
list_data = data[0].tolist()
all_starters = [0,1,2,3,4,5,6,7,8]
list_output = []
for k in range(9):
    list_loop = [k]
    for day in range(156):
        for i in range(len(list_loop)):
            if list_loop[i]==0:
                list_loop[i] = 6
                list_loop.append(8)
            else:
                list_loop[i] -= 1
    list_output.append(len(list_loop))

for day in range(100):
    for i in range(len(list_data)):
        if list_data[i]==0:
            list_data[i] = 6
            list_data.append(8)
        else:
            list_data[i] -= 1
    print(day)
len(list_data)
sum_result = 0
for i in range(9):
    sum_result+=list_data.count(i)*list_output[i]