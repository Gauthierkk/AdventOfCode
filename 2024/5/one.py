with open('input.txt', 'r') as f:
    parts = f.read().split('\n\n')
    
    ordering = {}

    for p in parts[0].split('\n'):
        nums = p.split('|')
        if int(nums[1]) not in ordering: ordering[int(nums[1])] = [int(nums[0])]
        else: ordering[int(nums[1])].append(int(nums[0]))
    
    output = 0

    for p in parts[1].split('\n'):
        nums = [int(x) for x in p.split(',')]
        flag = False
        
        for i, n in enumerate(nums):
            if flag: continue
            for m in nums[i:]:
                if n in ordering and m in ordering[n]:
                    flag = True
                    break

        if not flag: 
            middle = nums[int((len(nums)-1)/2)]
            output += middle

    print(output)
    
        
