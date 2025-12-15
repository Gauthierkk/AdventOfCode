def move(dir, steps, start) -> list[int]:

    print(f"Start: {start}, Dir: {dir}, Steps: {steps}")
    

    if steps > 100:
        output = steps // 100
        print("A")
    else:
        output = 0
    
    if output > 0 and start == 0: 
        output -= 1

    steps = steps % 100

    if dir == 'R':
        if start + steps > 100:
            print("B")
            output += 1
        start += steps
        
    else:
        if start != 0 and start - steps < 0:
            print("C")
            output += 1
        start -= steps

    start %= 100
    if start == 0:
        print("D")
        output += 1

    print(f"Start: {start}, output: {output}")
    print("-"*20)
        
    return [start, output]

with open('2025/1/input.txt') as f:
    start = 50
    lines = f.readlines()
    output = 0

    for line in lines:
        dir = line.strip()[0]
        steps = int(line.strip()[1:])
        int_list = move(dir, steps, start)
        
        start = int_list[0]
        output += int_list[1]
        print("Total output:", output)

    print(output)