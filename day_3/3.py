with open('3.txt', 'r') as f:
    data = f.read().splitlines()

priority = 0

for line in data:
    comp_1 = line[:len(line)//2]
    comp_2 = line[len(line)//2:]
    
    overlap = set(comp_1).intersection(comp_2).pop()
    
    if overlap.isupper():
        priority += ord(overlap) - 38
    elif overlap.islower():
        priority += ord(overlap) - 96
        
print(priority) # part 1 solution

priority = 0

for ind in range(0, len(data), 3):    
    elf1 = data[ind]
    elf2 = data[ind+1]
    elf3 = data[ind+2]
    
    badge = set(elf1).intersection(elf2).intersection(elf3).pop()
    
    if badge.isupper():
        priority += ord(badge) - 38
    elif badge.islower():
        priority += ord(badge) - 96

print(priority)
