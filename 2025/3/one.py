from pathlib import Path

# Read input file from the same directory as this script
input_file = Path(__file__).parent / 'input.txt'
with open(input_file, 'r') as f:
    lines = f.readlines()
    sum = 0

    for line in lines:
        line = line.strip()
        print(line)

        tens = 0
        curr_max = 0

        for i in line:            
            curr_max = max(curr_max, tens*10 + int(i))
            if int(i) > tens:
                tens = int(i)

        sum += curr_max

    print(f"Final Sum: {sum}")

            
        