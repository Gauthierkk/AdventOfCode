with open('2025/2/input.txt', 'r') as f:
    data = f.read().strip().replace('\n', '').split(',')
    sum = 0 
    for r in data:
        lower = r.split('-')[0]
        upper = r.split('-')[1]
        print(f'Range: {lower} to {upper}')

        for i in range(int(lower), int(upper) + 1):
            str_i = str(i)
            if len(str_i) % 2 == 0:
                mid = len(str_i) // 2
                first_half = str_i[:mid]
                second_half = str_i[mid:]
                
                if first_half == second_half:
                    print(str_i)
                    sum += int(str_i)

    print(f'Sum: {sum}')