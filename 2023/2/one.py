

with open('/Users/gauthier/Documents/Code/Advent/2/input.txt', 'r') as file:

    bag = {'b': 14, 'r': 12, 'g': 13}
    sum = 0

    def isValid(game) -> bool:
        
        while True:
            print(game)

            num = int(game[:game.find(' ')])
            if num > bag[game[game.find(',')-1:game.find(',')]]: return False

            game = game[game.find(',')+1:].strip()

            if game.find(',') == -1: break
              
        return True

    for game in file:
        id = int(game[game.find(' '):game.find(':')])

        game = game.replace('blue', 'b').replace('red', 'r').replace('green', 'g').replace(';', ',')[game.find(':')+2:]
        if isValid(game): sum = sum + id
        
    
    print(sum)
        


