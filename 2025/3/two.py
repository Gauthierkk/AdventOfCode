from pathlib import Path

# Read input file from the same directory as this script
input_file = Path(__file__).parent / 'input.txt'
with open(input_file, 'r') as f:
    data = f.readlines()

    total_sum = 0
    for line in data:
        line = line.strip()

        num_stack = []

        for char in line:
            digit = int(char)
            
            if len(num_stack) < 12:
                num_stack.append(digit)
            else:
                for j in range(len(num_stack)):
                    if j == 11 and digit > num_stack[j]:
                        num_stack.pop()
                        num_stack.append(digit)
                        break
                    if j < 11 and num_stack[j] < num_stack[j+1]:
                        num_stack.pop(j)
                        num_stack.append(digit)
                        break
                    
        
        current_number = int(''.join(map(str, num_stack)))
        total_sum += current_number

    print(f"Final Sum: {total_sum}")