from pathlib import Path

# Read input file from the same directory as this script
input_file = Path(__file__).parent / 'input.txt'
with open(input_file, 'r') as f:
    lines = f.readlines()
    sum = 0

    for line in lines:
        line = line.strip()

        j = 1
        a = line[0]
        b = line[j]

        max_num = 0
        print(f"Initial max_num: {max_num}")

        for i in range(len(line)-1):
            if i == j:
                j += 1
                continue

            while int(a + b) <= max_num and j < len(line)-1:
                j += 1
                b = line[j]
                if int(a + b) > max_num:
                    max_num = int(a + b)
                    print(max_num)
                    break
        
        print(f"Final max num: {max_num}")
        sum += max_num
    
    print(f"Final Sum: {sum}")

            
        