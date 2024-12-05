with open('input.txt') as f:
    num1 = []
    num2 = []
    lines = f.readlines()
    for line in lines:
        num1.append(int(line.strip().split()[0]))
        num2.append(int(line.strip().split()[1]))

    similarity_dict = {}
    total = 0


    for i in num1:
        if i in similarity_dict:
            total = total + (similarity_dict[i] * i)
        else:
            count = 0
            for j in num2:
                if i == j: count = count+1
            similarity_dict[i] = count
            total = total + (similarity_dict[i] * i)

    print(total)