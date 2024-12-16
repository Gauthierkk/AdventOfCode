import copy

def checkLoop(og_dirr, og_pos) -> bool:
    l_pos = og_pos.copy()
    l_dirr = copy.deepcopy(og_dirr)
    l_hash = copy.deepcopy(hash)

    if og_dirr == '<':
        if pos[0] in l_hash: l_hash[pos[0]].append(pos[1] - 1)
        else: l_hash[pos[0]] = [pos[1] - 1]

    if og_dirr == '>':
        if pos[0] in l_hash: l_hash[pos[0]].append(pos[1] + 1)
        else: l_hash[pos[0]] = [pos[1] + 1]

    if og_dirr == 'V':
        if pos[0]+1 in l_hash: l_hash[pos[0]+1].append(pos[1])
        else: l_hash[pos[0]+1] = [pos[1]]

    if og_dirr == '^':
        if pos[0]-1 in l_hash: l_hash[pos[0]-1].append(pos[1])
        else: l_hash[pos[0]-1] = [pos[1]]
        

    count = 0
    # print(og_pos, og_dirr, hash)
    # print(l_pos, l_dirr, l_hash)
    
    onGrid = True
    while(onGrid):

        if l_dirr == '^':
            for i in range(l_pos[0], -1, -1):

                if l_dirr == og_dirr and l_pos == og_pos: 
                    if count < 3: 
                        count += 1
                    else:
                        return True
                
                if i in l_hash and l_pos[1] in l_hash[i]:
                    l_dirr = '>'
                    break

                l_pos[0] = i
                
        if l_dirr == '>':
            for i in range(l_pos[1], len(grid[0])):

                if l_dirr == og_dirr and l_pos == og_pos: 
                    if count < 3: 
                        count += 1
                    else:
                        return True

                if l_pos[0] in l_hash and i in l_hash[l_pos[0]]:
                    l_dirr = 'V'
                    break

                l_pos[1] = i
                    
        if l_dirr == 'V':
            for i in range(l_pos[0], len(grid)):
                if l_dirr == og_dirr and l_pos == og_pos: 
                    if count < 3: 
                        count += 1
                    else:
                        return True
                
                if i in l_hash and l_pos[1] in l_hash[i]:
                    l_dirr = '<'
                    break

                l_pos[0] = i
            
        if l_dirr == '<':

            for i in range(l_pos[1], -1, -1):

                if l_dirr == og_dirr and l_pos == og_pos: 
                    if count < 3: 
                        # print('here')
                        count += 1
                    else:
                        # print(og_pos) 
                        return True
                
                if l_pos[0] in l_hash and i in l_hash[l_pos[0]]:
                    l_dirr = '^'
                    break

                l_pos[1] = i
                # print(l_dirr, l_pos)

        if l_pos[0] < 1 or l_pos[0] == len(grid)-1 or l_pos[1] < 1 or l_pos[1] == len(grid[0])-1:
            onGrid = False

    return False


with open ('input.txt') as f:

    hash = {}
    str = f.read()
    dirr = '^'
    loopPos = {}
    output = 0

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
    
    onGrid = True
    while(onGrid):

        if dirr == '^':
            for i in range(pos[0], -1, -1):
                
                if i in hash and pos[1] in hash[i]:
                    dirr = '>'
                    break

                pos[0] = i
                if checkLoop(dirr, pos):
                    output += 1
                    print(output, pos)
                # print(dirr, pos)
            
        if dirr == '>':
            for i in range(pos[1], len(grid[0])):
                if pos[0] in hash and i in hash[pos[0]]:
                    dirr = 'V'
                    break

                pos[1] = i
                if checkLoop(dirr, pos):
                    output += 1
                    print(output, pos)
                # print(dirr, pos)
                    
        if dirr == 'V':
            for i in range(pos[0], len(grid)):
                
                if i in hash and pos[1] in hash[i]:
                    dirr = '<'
                    break

                pos[0] = i
                if checkLoop(dirr, pos):
                    output += 1
                    print(output, pos)
                # print(dirr, pos)
            
        if dirr == '<':
            for i in range(pos[1], -1, -1):
                
                if pos[0] in hash and i in hash[pos[0]]:
                    dirr = '^'
                    break

                pos[1] = i
                # if pos == [8,4] and checkLoop(dirr, pos):
                if checkLoop(dirr, pos):
                    output += 1
                    print(output, pos)

                # print(dirr, pos)
               


        if pos[0] < 1 or pos[0] == len(grid)-1 or pos[1] < 1 or pos[1] == len(grid[0])-1:
            onGrid = False

print(output)