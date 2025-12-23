from pathlib import Path

input_file = Path(__file__).parent / 'input.txt'
with open(input_file, 'r') as f:
    lines = f.read()

    ranges = [[int(i) for i in r.split('-')] for r in lines.split('\n\n')[0].split('\n')]
    candidates = [int(i) for i in lines.split('\n\n')[1].split('\n')]
    ranges.sort()

    new_ranges = []

    for r in ranges:

        processed = False

        if not new_ranges:
            new_ranges.append(r)
            continue

        for n in new_ranges:

            if r[1] < n[0] or r[0] > n[1]:
                continue

            if r[0] >= n[0] and r[1] <= n[1]:
                processed = True
                break

            if r[1] > n[1]:
                n[1] = r[1]
                processed = True
                break
        

        if not processed:
            new_ranges.append(r)

    sum = 0
    for r in new_ranges:
        sum += r[1] - r[0] + 1

    print(sum)