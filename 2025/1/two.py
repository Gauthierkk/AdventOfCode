with open('2025/1/input.txt') as f:
    pos = 50
    lines = f.readlines()
    output = 0

    for line in lines:
        dir = line.strip()[0]
        steps = int(line.strip()[1:])

        for i in range(steps):
            if dir == 'R':
                pos += 1
            elif dir == 'L':
                pos -= 1

            if pos == 100 or pos == -100:
                pos = 0
                
            if pos == 0:
                output += 1

        
    print(output)