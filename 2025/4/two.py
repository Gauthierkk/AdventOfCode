from pathlib import Path

# Read input file from the same directory as this script
input_file = Path(__file__).parent / 'input.txt'
with open(input_file, 'r') as f:
    lines = f.readlines()

    grid = []
    for line in lines:
        grid.append(list(line.strip()))

    total_removed = 0

    while True:
        print("=" * 20)
        print(f"Removed so far: {total_removed}")
        rolls_removable_this_pass = 0

        # for row in grid:
        #     print("".join(row))

        coords_to_remove = []

        for x, row in enumerate(grid):
            for y, cell in enumerate(row):    
                if cell == "@":
                    count_adjacent = 0

                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue
                            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                                if grid[x + dx][y + dy] == "@":
                                    count_adjacent += 1

                    if count_adjacent < 4:
                        coords_to_remove.append((x, y))
                        rolls_removable_this_pass += 1
        
        for x, y in coords_to_remove:
            grid[x][y] = "."

        if rolls_removable_this_pass == 0:
            break
            
        total_removed += rolls_removable_this_pass

        print(f"Rolls removed this pass: {rolls_removable_this_pass}")

        

    print(f"Total Removed: {total_removed}")