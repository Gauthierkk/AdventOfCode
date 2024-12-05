ordering = {}
reverse_ordering = {}

def inOrder(nums) -> bool:
    flag = False
    
    for i, n in enumerate(nums):
        if flag: continue
        for m in nums[i:]:
            if n in reverse_ordering and m in reverse_ordering[n]:
                flag = True
                break

    return not flag

def order(nums) -> int:
    zeros = [0] * len(nums)
    priority = dict(zip(nums, zeros))

    for n in nums:
        if n in ordering:
            for m in ordering[n]:
                if m in nums: priority[n] += 1

    priority = dict(sorted(priority.items(), key=lambda item: item[1]))
    newNums = list(reversed(priority.keys()))
    
    return newNums[int((len(nums)-1)/2)]

with open('input.txt', 'r') as f:
    parts = f.read().split('\n\n')
    
    for p in parts[0].split('\n'):
        nums = p.split('|')
        if int(nums[0]) not in ordering: ordering[int(nums[0])] = [int(nums[1])]
        else: ordering[int(nums[0])].append(int(nums[1]))

        if int(nums[1]) not in reverse_ordering: reverse_ordering[int(nums[1])] = [int(nums[0])]
        else: reverse_ordering[int(nums[1])].append(int(nums[0]))
    
    output = 0
    count = 0

    for p in parts[1].split('\n'):
        count +=1
        nums = [int(x) for x in p.split(',')]

        if inOrder(nums): continue

        output += order(nums)
    
    print(output)

    
        
