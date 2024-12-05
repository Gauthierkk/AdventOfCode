import re

with open('/Users/gauthier/Documents/Code/Advent/3/test.txt', 'r') as file:

    file = file.readlines()
    sum = 0

    #line number
    for i, line in enumerate(file):

        #remove trailing newline
        line = line.strip()

        #characters in line
        for j, c in enumerate(line):
            
            #check if it's a number (specifically the final digit, then find the rest)
            if c.isdigit() and (j+1 == len(line) or not line[j+1].isdigit()):
                s = j
                while line[s-1].isdigit() and s > -1: s = s-1

                num = line[s:j+1]
                
                #check surrounding 
                symbol = []
                for l in range(i-1,i+2):
                    
                    if l == -1: continue
                    if l == len(file): break

                    for m in range(s-1,j+2):
                        if m == -1: continue
                        if m == len(line): break

                        if not file[l][m].isdigit() and not file[l][m] == '.': sum = sum + int(num)
                    

    print(sum)


                
                    
                    
              
            