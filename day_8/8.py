import numpy as np

with open('8.txt', 'r') as f:
    forest = f.read().splitlines()
    
forest = [list(x) for x in forest] # convert line to list

forest_np = np.array(forest)
forest_np = forest_np.astype(int)

count_visible = 0
max_score = 0
for idx, row in enumerate(forest[1:-1]):
    
    for idy, column in enumerate(row[1:-1]):
        
        # part 1
        tree = forest_np[idx+1, idy+1]
        tree_right = max(forest_np[idx+1,idy+2:])
        tree_left = max(forest_np[idx+1,:idy+1])   
        tree_down = max(forest_np[idx+2:,idy+1])
        tree_up = max(forest_np[:idx+1, idy+1])
        
        if tree <= min(tree_right, tree_left, tree_down, tree_up):
            count_visible += 1
            
        # part 2
        for i in range(idy+2,98): # trees right
            if tree <= forest_np[idx+1, i]: break
        score = i-idy-1
        for i in range(1, idy+2): # trees left
            if tree <= forest_np[idx+1, idy+1-i]: break
        score *= i
        for i in range(idx+1, 98): # trees down
            if tree <= forest_np[i+1, idy+1]: break
        score *= i-idx
        for i in range(1, idx+2): # trees up
            if tree <= forest_np[idx+1-i, idy+1]: break
        score *= i
        
        if score > max_score: max_score = score
        
        
print(99*99 - count_visible) # part 1 solution   
print(max_score) # part 2 solution      
