from pathlib import Path

# Read input file from the same directory as this script
input_file = Path(__file__).parent / 'input.txt'
with open(input_file, 'r') as f:
    lines = f.readlines()

print(lines)
