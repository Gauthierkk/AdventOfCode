output = 0

def isSafe (nums) -> bool:
    increasing = True
    
    for i, n in enumerate(nums):
        if i == 0: continue

        if i == 1 and int(n) < int(nums[i-1]): increasing = False
        elif i > 1:
            if increasing and int(n) < int(nums[i-1]):
                return False
            elif not increasing and int(n) > int(nums[i-1]):
                return False
            
        temp = abs(int(n) - int(nums[i-1]))
        if temp < 1 or temp > 3:
            return False
        
    return True

with open('input.txt') as f:
    for line in f.readlines():
        nums = line.strip().split()
        safe = False

        if isSafe(nums):
            output += 1
            continue

        for i in range(len(nums)):
            if isSafe(nums[:i] + nums[i+1:]):
                safe = True
                break
        
        if safe: output += 1

print(output)
