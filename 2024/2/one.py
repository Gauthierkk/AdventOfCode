output = 0

with open('input.txt') as f:
    for line in f.readlines():
        nums = line.strip().split()

        increasing = True
        safe = True
        
        for i, n in enumerate(nums):
            if i == 0: continue

            if i == 1 and int(n) < int(nums[i-1]): increasing = False
            elif i > 1:
                if increasing and int(n) < int(nums[i-1]):
                    safe = False
                    break
                elif not increasing and int(n) > int(nums[i-1]):
                    safe = False
                    break

            temp = abs(int(n) - int(nums[i-1]))
            if temp < 1 or temp > 3:
                safe = False
                break

        if safe: output += 1

print(output)