def process(input : str) -> int:
    
    str = input.split("mul")
    output = 0

    for s in str:
        if len(s) == 0 or s[0] != '(' or s.find(')') == -1 or s.find(',') == -1:
            continue

        try:
            num1 = int(s[s.find('(')+1:s.find(',')])
            num2 = int(s[s.find(',')+1:s.find(')')])
        except:
            continue

        output += num1 * num2
    
    return output

with open('input.txt', 'r') as f:

    file = f.read()
    str = file.split("don't()")

    output = process(str[0])

    for s in str[1:]:
        s = s[s.find("do()"):]
        output += process(s)
        

    print(output)


    
