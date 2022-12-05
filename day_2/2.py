import pandas as pd

lines = pd.read_csv('2.csv')

di1 = {'A':1, 'B':2, 'C':3}
di2 = {'X':1, 'Y':2, 'Z':3}
  
lines['move'] = lines['move'].map(di1)
lines['response'] = lines['response'].map(di2)
lines['score'] = 0

for index, row in lines.iterrows():
    if (row['move'] - row['response'] in (-1, 2)): # win
        row['score'] = row['response'] + 6    
    elif (row['move'] == row['response']): # draw
        row['score'] = row['response'] + 3
    else: # lose
        row['score'] = row['response']
        
print(sum(lines['score'])) # part 1 solution

lines['score'] = 0

for index, row in lines.iterrows():
    if (row['response'] == 2): # draw
        row['score'] = row['draw'] + 3
        
    elif (row['response'] == 1): # lose
        if (row['move'] == 1):
            row['score'] = 3
        elif (row['move'] == 2):
            row['score'] = 1
        elif (row['move'] == 3):
            row['score'] = 2       
   
    elif (row['response'] == 3): # win
        if (row['move'] == 1):
            row['score'] = 8
        elif (row['move'] == 2):
            row['score'] = 9
        elif (row['move'] == 3):
            row['score'] = 7

print(sum(lines['score'])) # part 2 solution