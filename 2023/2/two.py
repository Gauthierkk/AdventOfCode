import re

with open('/Users/gauthier/Documents/Code/Advent/2/input.txt', 'r') as file:

    sum = 0

    def fewest(games):

        add = 1
        bag = {'b': 0, 'r': 0, 'g': 0}
        
        for i in games:
            val = int(i[:i.find(' ')])
            if bag[i[-1]] == 0: bag[i[-1]] = val
            elif bag[i[-1]] < val: bag[i[-1]] = val

        for k in bag: add = add * bag[k]
        return add

    for game in file:
        id = int(game[game.find(' '):game.find(':')])

        game = game.replace('blue', 'b').replace('red', 'r').replace('green', 'g')[game.find(':')+2:]

        games = [i.strip() for i in re.split(';|,', game)]
        
        add = fewest(games)
        sum = sum + add


    print(sum)        
    
        


