maps = []

def map(seed) -> int:

    out = seed
    for m in maps:
        for range in m:
            dest = range[0]
            source = range[1]
            step = range[2]        

            if source <= out and out < (source+step):
                diff = out-source
                out = dest + diff
                break
    return out

with open('input.txt') as f:
    str = f.read()
    minimum = None

    almanac = str.split('\n\n')

    seeds = [int(n) for n in almanac[0].split(":")[1].split()]

    for x in range(1, 8):
        maps.append([[int(i) for i in n.split()] for n in almanac[x].split(":")[1].strip().split('\n')])

    for s in seeds:
        curr = map(s)
        minimum = min(minimum, curr) if minimum else curr

    print(minimum)
    