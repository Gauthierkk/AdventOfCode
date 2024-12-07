def eval(val, nums) -> int:
    results = [nums[0]]

    for n in nums[1:len(nums)-1]:
        newResults = []
        for r in results:
            newResults.append(n+r)
            newResults.append(n*r)

        
        results = newResults
    
    for r in results:
        if r + nums[-1] == val or r * nums[-1] == val: return val
    return -1
    

with open('input.txt', 'r') as f:
    output = 0

    for line in f.readlines():
        str = line.split(':')
        val = int(str[0].strip())
        nums = [int(n) for n in str[1].split()]

        curr = eval(val, nums)
        if curr > 0:
            output += curr

    print("results: ", output)