def eval(val, nums):
    results = [nums[0]]

    for n in nums[1:len(nums)-1]:
        newResults = []
        for r in results:
            print(r)
            
            valStr = str(val)
            rStr = str(r)
            if rStr in valStr: print(rStr, valStr)

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
        print(results)
        for r in results:
            if r + nums[-1] == val or r * nums[-1] == val: 
                print(val, nums)
                output+= val
                break
                

    print("Final: ", output)