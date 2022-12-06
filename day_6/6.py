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