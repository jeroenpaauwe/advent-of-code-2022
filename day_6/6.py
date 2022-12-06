with open("day_6/6.txt") as f:
    signal = f.read()

for i in range(0,len(signal)-3):
    packet = signal[i:i+4]
    if len(set(packet)) == 4:
        break
        
print(i+4) # solution part 1
    
for i in range(0,len(signal)-13):   
    packet = signal[i:i+14]
    if len(set(packet)) == 14:
        break
        
print(i+14) # solution part 2

packets = [set(signal[i:i+4]) for i in range(0,len(signal)-3)]

fours = [len(x) for x in packets]

print(fours.index(4)+4) # solution part 1 (using list comprehension)

packets = [set(signal[i:i+14]) for i in range(0,len(signal)-13)]

fourteens = [len(x) for x in packets]

print(fourteens.index(14)+14) # solution part 2 (using list comprehension)

