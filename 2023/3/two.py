import re

with open('/Users/gauthier/Documents/Code/Advent/3/input.txt', 'r') as file:

    file = file.readlines()
    sum = 0

    #line number
    for i, line in enumerate(file):

        #remove trailing newline
        line = line.strip()

        #characters in line
        for j, c in enumerate(line):
            
            #check if it's a star
            if c == '*':
                
                nums = []

                #gather rows
                rows=[i-1, i, i+1]

                #loop through rows
                for r in rows:
                    #row edge cases
                    if r == -1: continue
                    if r == len(file): break

                    #top and bottom row middle digit case
                    if file[r][j].isdigit() and r is not i:
                        right, left = j, j
                        while right + 1 < len(file[r]) and file[r][right].isdigit(): right = right + 1
                        while left > 0 and file[r][left].isdigit(): left = left-1
                        nums.append(int(file[r][left+1:right]))

                    #if no middle col number (or middle row) just check right and left
                    else:
                        #right
                        if j+1 < len(line) and file[r][j+1].isdigit():
                            s = j
                            while s+1 < len(file[r]) and file[r][s+1].isdigit(): s = s+1
                            nums.append(int(file[r][j+1:s+1]))
                        if j > 0 and file[r][j-1].isdigit():
                            s = j
                            while file[r][s-1].isdigit() and s > -1: s = s-1
                            nums.append(int(file[r][s:j]))

                if len(nums) == 2: sum = sum + nums[0]*nums[1]           

    print(sum)


                
                    
                    
              
            