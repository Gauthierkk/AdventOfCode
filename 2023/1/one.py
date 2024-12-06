import re

with open('/Users/gauthier/Documents/Code/Advent/1/input.txt', 'r') as file:

    sum = 0

    for s in file:

        p = 0

        for c in s:
            if c.isdigit():
                p = p + int(c)*10
                break

        for c in reversed(s):
            if c.isdigit():
                p = p + int(c)
                break
        
        print(p)
        sum = sum + p
    
    print(sum)
        

