with open('/Users/gauthier/Documents/Code/Advent/4/input.txt', 'r') as file:

    file = file.readlines()
    sum = 0

    for line in file:
        
        myNums = set(line[line.find(':')+1:line.find('|')].strip().replace('  ', ' ').split(' '))
        wNums = set(line[line.find('|')+1:].strip().split(' '))
        common = myNums & wNums
        pts = pow(2, len(common)-1) if common else 0
        sum = sum + pts
    
    print(sum)