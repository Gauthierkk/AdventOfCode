def eval(val, nums):
    results = [nums[0]]

    for n in nums[1:]:
        newResults = []
        for r in results:

            if not (n+r) > val: newResults.append(n+r)
            if not (n*r) > val: newResults.append(n*r)

        results = newResults

    return results
    

with open('input.txt', 'r') as f:
    output = 0

    for line in f.readlines():
        string = line.split(':')
        val = int(string[0].strip())
        nums = [int(n) for n in string[1].split()]

        results = eval(val, nums)
        if val in results[-2:]: output += val
                

    print("Final: ", output)

