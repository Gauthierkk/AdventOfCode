from pathlib import Path

input_file = Path(__file__).parent / 'input.txt'
with open(input_file, 'r') as f:
    lines = f.read()

    ranges = [[int(i) for i in r.split('-')] for r in lines.split('\n\n')[0].split('\n')]
    candidates = [int(i) for i in lines.split('\n\n')[1].split('\n')]
    ranges.sort()

    output = 0

    for c in candidates:
        for r in ranges:
            if c >= r[0] and c <= r[1]:
                output += 1
                break

                b


    print(output)