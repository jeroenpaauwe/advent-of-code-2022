import numpy as np

with open('9.txt', 'r') as f:
    instructions = f.read().splitlines()
    
dic = {'U':[0,1],'D':[0,-1],'L':[-1,0],'R':[1,0]}
head = [[0,0]]
tail = [[0,0]]
    
def head_move(direction):
    end = np.array(head[-1]) + np.array(direction)
    head.append(end)
          
def tail_move(h, t):
    h = np.array(h)
    t = np.array(t)
    
    d = h - t
    if sum(abs(d)) == 2 and not np.all(d): # horizontal or vertical move
        tail.append(t + d/2)
    if sum(abs(d)) > 2: # diagonal move
        x = -1 if d[0] < 0 else 1
        y = -1 if d[1] < 0 else 1
        d = np.array([x,y])
        tail.append(t + d)

for move in instructions:
    
    direction, magnitude = move.split()
    direction = dic[direction]
    
    for i in range(1, int(magnitude)+1):
        head_move(direction)
        tail_move(head[-1], tail[-1])
        
unique_tail = [str(x) for x in tail]
print(len(set(unique_tail))) # solution part 1


