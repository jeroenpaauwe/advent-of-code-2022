import re

with open('4.txt', 'r') as f:
    data = f.read().splitlines()
    
count = 0

for line in data:
    groups = list(map(int, re.split(',|-', line)))
    
    if (groups[0] >= groups[2]) & (groups[1] <= groups[3]):
        count += 1
    elif (groups[2] >= groups[0]) & (groups[3] <= groups[1]):
        count += 1
    
print(count) # part 1 solution

with open("4.txt", "r") as f:
    data = re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", f.read())
    data = [[int(e) for e in row] for row in data]

overlap = [max(a, c) <= min(b, d) for a, b, c, d in data]

print(sum(overlap))  # part 2 solution