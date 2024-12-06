maps = []

def map(seeds) -> int:

    print(seeds)

    for m in maps:
        for range in m:
            dest = range[0]
            dest_end = dest + range[2]        

            source = range[1]
            source_end = source + range[2]

    return 1

with open('input.txt') as f:
    str = f.read()
    minimum = None

    almanac = str.split('\n\n')

    seedranges = [int(n) for n in almanac[0].split(":")[1].split()]
    seeds = []

    for i in range(0,len(seedranges), 2):
        seeds.append([seedranges[i], seedranges[i]+seedranges[i+1]])

    print(seeds)

    for x in range(1, 8):
        maps.append([[int(i) for i in n.split()] for n in almanac[x].split(":")[1].strip().split('\n')])

    for range in seeds:
        curr = map(range)
        

    print(minimum)
    