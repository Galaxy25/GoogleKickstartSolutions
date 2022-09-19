from collections import *

def durSort(e):
    return int(e[0][1])
def idSort(e):
    return int(e[2])
cases = int(input())
for case in range(cases):
    fabricsC = defaultdict(lambda: [])
    fabricsA = defaultdict(lambda: [])
    for i in range(int(input())):
        fabric = input().split(" ")
        fabricsC[fabric[0]].append(fabric)
        fabricsA[fabric[1]].append(fabric)
    fabricsC = list(fabricsC.values())
    fabricsA = list(fabricsA.values())
    fabricsC.sort()
    fabricsA.sort(key=durSort)
    comC = []
    comA = []
    total = 0
    for i in range(len(fabricsC)):
        comC.extend(sorted(fabricsC[i], key=idSort))
    for i in range(len(fabricsA)):
        comA.extend(sorted(fabricsA[i], key=idSort))
    for i, u in zip(comC, comA):
        if i == u:
            total += 1
    print(f"Case #{case + 1}: {total}")