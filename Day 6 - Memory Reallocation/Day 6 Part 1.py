import pandas as pd
banks = pd.read_csv("day6.txt",delimiter = "\t",header = None)
banks = banks.iloc[0,:]
banks = list(banks)
configs = []
while banks not in configs:
    configs.append(list(banks))
    big_boy = max(banks)    
    big_boy_spots = [i for i in range(len(banks)) if banks[i] == big_boy]
    #ties broken by lowest bank number
    big_boy_index = big_boy_spots[0]
    banks[big_boy_index] = 0
    for i in range(1,big_boy+1):
        banks[(big_boy_index + i) % len(banks)] = banks[(big_boy_index + i) % len(banks)] + 1 
print(len(configs))