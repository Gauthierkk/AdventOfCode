with open('input.txt') as f:

    letters = []

    for line in f.readlines():
        letters.append(line.strip())

    height = len(letters)
    width = len(letters[0])

    output = 0

    for i in range(height):
        for j in range(width):
            if letters[i][j] == 'X':
                for x in range(-1, 2):                
                    for y in range(-1, 2):
                        if -1 < i+x < height and -1 < j+y < width and letters[i+x][j+y] == 'M':
                            if -1 < i+2*x < height and -1 < j+2*y < width and letters[i+2*x][j+2*y] == 'A':
                                if -1 < i+3*x < height and -1 < j+3*y < width and letters[i+3*x][j+3*y] == 'S':
                                    output += 1
    
    print(output)
 
