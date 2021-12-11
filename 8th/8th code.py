import pandas as pd
import os 
import numpy as np
from itertools import permutations

path, filename = os.path.split(os.path.realpath(__file__))


#1st
data = pd.read_csv(path + '/input.txt', delimiter=" | ", skiprows=0, error_bad_lines=False, header=None, squeeze=True)
count=0

for index, row in data.iloc[:,-4:].iterrows():
    count += sum(row.str.len().isin([2,3,4,7]))


#2nd

letters = ["a","b","c","d","e","f","g"]
df = pd.DataFrame(letters)


correct = {
		0 : "abcefg",
		1 : "cf",
		2 : "acdeg",
		3 : "acdfg",
		4 : "bcdf",
		5 : "abdfg",
        6 : "abdefg",
        7 : 'acf',
        8 : 'abcdefg',
        9 : 'abcdfg'}    
correct_inv = dict(zip(correct.values(),correct.keys()))
unique_comb = [''.join(p) for p in permutations('abcdefg')]
correct_list = []
sum_code = 0
for index, row in data.iloc[:,:-5].iterrows():
    code = []
    for combination in unique_comb:
        translation = {
        		combination[0] : "a",
        		combination[1] : "b",
        		combination[2] : "c",
        		combination[3] : "d",
        		combination[4] : "e",
        		combination[5]:  "f",
                combination[6] : "g"}    
        for cell in row:
           trans_char = []
           for char in cell:
               trans_char += translation[char]
           if ''.join(sorted(trans_char)) not in correct.values():
               break
           if cell == row.iloc[-1]:
               print(translation)
               correct_list.append(translation)
               for cell in data.iloc[index,-4:]:
                   trans_char_code = []
                   for char in cell:
                      trans_char_code += translation[char]
                   code +=  str(correct_inv[''.join(sorted(trans_char_code))])
               sum_code += int((''.join(code)))