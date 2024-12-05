with open('input.txt') as f:

    letters = []

    for line in f.readlines():
        letters.append(line.strip())

    height = len(letters)
    width = len(letters[0])

    output = 0

    for i in range(height):
        for j in range(width):
            if letters[i][j] == 'A':
                if i < 1 or j < 1 or i+1 == height or j+1 == width: continue

                corners = []
                corners.append(letters[i-1][j-1])
                corners.append(letters[i-1][j+1])
                corners.append(letters[i+1][j+1])
                corners.append(letters[i+1][j-1])

                if not all(l in ['M','S'] for l in corners):
                    continue
                
                if corners.count('M') != 2:
                    continue

                if corners[0] == corners[2]: 
                    continue

                output += 1



    print(output)