with open("6.txt") as f:
   signal = f.read()

for i in range(0,len(signal)-3):   
    if (signal[i:i+4].count(signal[i]) == 1 and signal[i:i+4].count(signal[i+1]) == 1 and 
        signal[i:i+4].count(signal[i+2]) == 1 and signal[i:i+4].count(signal[i+3]) == 1):
        break
        
print(i+4) # solution part 1
    
for i in range(0,len(signal)-13):   
    if (signal[i:i+14].count(signal[i]) == 1 and signal[i:i+14].count(signal[i+1]) == 1 and 
        signal[i:i+14].count(signal[i+2]) == 1 and signal[i:i+14].count(signal[i+3]) == 1 and
        signal[i:i+14].count(signal[i+4]) == 1 and signal[i:i+14].count(signal[i+5]) == 1 and
        signal[i:i+14].count(signal[i+6]) == 1 and signal[i:i+14].count(signal[i+7]) == 1 and
        signal[i:i+14].count(signal[i+8]) == 1 and signal[i:i+14].count(signal[i+9]) == 1 and
        signal[i:i+14].count(signal[i+10]) == 1 and signal[i:i+14].count(signal[i+11]) == 1 and
        signal[i:i+14].count(signal[i+12]) == 1 and signal[i:i+14].count(signal[i+13]) == 1):
        break
        
print(i+14) # solution part 1