with open('input.txt') as f:

    str = f.read().split("mul")
    output = 0

    for s in str:
        if s[0] != '(' or s.find(')') == -1 or s.find(',') == -1:
            continue
        
        try:
            num1 = int(s[s.find('(')+1:s.find(',')])
            num2 = int(s[s.find(',')+1:s.find(')')])
        except:
            continue

        output += num1 * num2

print(output)