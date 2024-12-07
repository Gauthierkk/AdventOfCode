with open ('input.txt') as f:

    hash = {}
    visited = {}
    str = f.read()
    dirr = '^'

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

                if i not in visited: visited[i] = {pos[1]}
                else: visited[i].add(pos[1])

                pos[0] = i
            
        if dirr == '>':
            for i in range(pos[1], len(grid[0])):
                if pos[0] in hash and i in hash[pos[0]]:
                    dirr = 'V'
                    break

                if pos[0] not in visited: visited[pos[0]] = {i}
                else: visited[pos[0]].add(i)

                pos[1] = i
                    
        if dirr == 'V':
            for i in range(pos[0], len(grid)):
                
                if i in hash and pos[1] in hash[i]:
                    dirr = '<'
                    break

                if i not in visited: visited[i] = {pos[1]}
                else: visited[i].add(pos[1])

                pos[0] = i
            
        if dirr == '<':
            for i in range(pos[1], -1, -1):
                
                if pos[0] in hash and i in hash[pos[0]]:
                    dirr = '^'
                    break
                    
                if pos[0] not in visited: visited[pos[0]] = {i}
                else: visited[pos[0]].add(i)

                pos[1] = i

        if pos[0] < 1 or pos[0] == len(grid)-1 or pos[1] < 1 or pos[1] == len(grid[0])-1:
            onGrid = False

    output = 0
    for k in visited:
        output += len(visited[k])

    print(output)