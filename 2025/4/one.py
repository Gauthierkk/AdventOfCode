from pathlib import Path

# Read input file from the same directory as this script
input_file = Path(__file__).parent / 'input.txt'
with open(input_file, 'r') as f:
    lines = f.readlines()

    grid = []
    for line in lines:
        grid.append(list(line.strip()))

    total_rolls_removable = 0

    for x, row in enumerate(grid):
        for y, cell in enumerate(row):    
            if cell == "@":
                count_adjacent = 0

                # print("=" * 20)
                # print(f"Found '@' at ({x}, {y})")

                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                            if grid[x + dx][y + dy] == "@":
                                count_adjacent += 1

                # print(f"Number of adjacent '@': {count_adjacent}")
                if count_adjacent < 4:
                    total_rolls_removable += 1

    print(f"Total '@' that can be removed: {total_rolls_removable}")