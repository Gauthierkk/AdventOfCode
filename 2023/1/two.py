import re

with open('/Users/gauthier/Documents/Code/Advent/1/input.txt', 'r') as file:

    final = 0
    numbers = {'one': 1, 'two': 2,'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    for s in file:

        sum = 0
       
        for k in numbers:
            s = s.replace(k, k + str(numbers[k]) + k)

        print(s)

        for c in s:
            if c.isdigit():
                sum = sum + int(c)*10
                break

        for c in reversed(s):
            if c.isdigit():
                sum = sum + int(c)
                break

        print(sum)
        final = final + sum
        
    print(final)
        

