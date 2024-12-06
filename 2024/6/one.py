with open ('input.txt') as f:

    hash = {}
    visited = []
    str = f.read()
    dirr = 1

    grid = str.split('\n')
    
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '#':
                try:
                    hash[x].append(y)
                except:
                    hash[x] = [y]
            if grid[x][y] == '^':
                pos = [x, y]
    
    while(True):

        for i in range(pos[0], -1, -1):
            if grid[pos[0]] 

            if i in hash and pos[1] in hash[i]:
                dirr = 2
                break
        
        break