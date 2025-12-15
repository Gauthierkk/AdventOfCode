def checkPattern(num: int) -> bool:
    num_str = str(num)
    length = len(num_str)

    if num_str[0] == '0':
        return False

    for j in range(length//2):
        curr = num_str[:j+1]

        if length % len(curr) != 0:
            continue

        times = length // len(curr)
        pattern = curr * times
        if pattern == num_str:
            return True

    return False


with open('2025/2/input.txt', 'r') as f:
    data = f.read().strip().replace('\n', '').split(',')
    sum = 0
    max_num = 0
    ranges = []

    for r in data:
        lower = r.split('-')[0]
        upper = r.split('-')[1]
        ranges.append((int(lower), int(upper)))

    for lower, upper in ranges:
        print(f'Checking numbers from range {lower}-{upper}')
        for i in range(lower, upper+1):
            if checkPattern(i):
                print(f'Found pattern number: {i}')
                sum += i

    print(f'Sum: {sum}')
