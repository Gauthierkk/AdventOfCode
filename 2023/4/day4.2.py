import re

with open('/Users/gauthier/Documents/Code/Advent/4/input.txt', 'r') as file:

    file = file.readlines()
    sum = 0
    game_count = {1:0}


    for i, line in enumerate(file):
        
        #find game ID
        id = int(re.findall(r'\d+', line[:line.find(':')])[0])
        game_count[id] = game_count[id] + 1 if id in game_count else 1

        #Extract your hand and winning numbers
        myNums = set(line[line.find(':')+1:line.find('|')].strip().replace('  ', ' ').split(' '))
        wNums = set(line[line.find('|')+1:].strip().split(' '))
        
        #Find the winning numbers
        common = myNums & wNums 

        #Loop through number of copies of current set
        for copies in range(game_count[id]):
            
            #keep tally of total cards
            sum = sum+1
            
            #For each copy of the game, do the math on winning nums
            for j, c in enumerate(common):

                game_count[id+j+1] = game_count[id+j+1] + 1 if id+j+1 in game_count else 1
        
    print(sum)
