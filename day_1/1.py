import pandas as pd

lines = pd.read_csv('1.csv', skip_blank_lines=False)

total = 0
total_list = []
   
for index, row in lines.iterrows():
    if not pd.isna(row['calories']):
        total += row['calories']
    else:
        total_list.append(total)
        total = 0

print(max(total_list)) # answer part 1

total_list.sort(reverse=True)

print(sum(total_list[0:3]))
