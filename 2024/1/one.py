with open('input.txt') as f:
    num1 = []
    num2 = []
    lines = f.readlines()
    for line in lines:
        num1.append(int(line.strip().split()[0]))
        num2.append(int(line.strip().split()[1]))
        # print(num1[-1], num2[-1])

    num1.sort()
    num2.sort()
    distance = 0
    for i in range(len(num1)):
        distance = distance + abs(num1[i] - num2[i])

    print(distance)
        