import pandas as pd

df = pd.read_csv('day2.txt', sep='\t', header = None)

checksum = 0
for i in df.index:
    the_min = min(df.iloc[i,:])
    the_max = max(df.iloc[i,:])
    checksum = checksum + (the_max - the_min)
    
print(checksum)