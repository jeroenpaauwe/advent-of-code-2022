with open('10.txt', 'r') as f:
    file = f.read().splitlines()

x = 1
c = 0
total = 0
 
def parse_instruction(line):
    if line == 'noop':
        dx = 0
        dc = 1
    else:
        coordinate, dx = line.split()
        dx = int(dx)
        dc = 1
    return dx, dc

for i in file:
    dx, dc = parse_instruction(i)
    
    if dx != 0: # noop
        c += dc
        if c in (20, 60, 100, 140, 180, 220):
            total += x * c
                  
    c += dc
    
    if c in (20, 60, 100, 140, 180, 220):
        total += x * c
        
    x += dx
    
print(total) # solution part 1

c = 0
sprite = [0,1,2]
crt = list("." * 40 * 6)

for j in file:
    dx, dc = parse_instruction(j)
           
    # draw pixel
    if c in sprite:
        crt[c] = 'X'
    
    # finish cycle, move crt
    c += dc
    if c / 40 in (1,2,3,4,5,6): # new line
        sprite = [i + 40 for i in sprite]
    
    if dx != 0: # addx instruction
        # draw pixel
        if c in sprite:
            crt[c] = 'X'
        
        # move sprite
        sprite = [i + dx for i in sprite]
    
        # finish cycle, move crt
        c += dc
        if c / 40 in (1,2,3,4,5,6): # new line
            sprite = [i + 40 for i in sprite]


print(crt)

