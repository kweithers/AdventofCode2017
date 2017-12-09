import pandas as pd
from itertools import product

df = pd.read_csv('day2.txt', sep='\t', header = None)

checksum = 0
for i in df.index:
    for j,k in product(range(len(df.columns)),range(len(df.columns))):
        if k==j:
            continue 
        if df.iloc[i,j] % df.iloc[i,k] == 0:
            checksum = checksum + df.iloc[i,j] / df.iloc[i,k]
            break
    
print(checksum)