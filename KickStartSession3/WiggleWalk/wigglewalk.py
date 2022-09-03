for case in range(int(input())):
    matrixInfo = input().split()
    matrixInfo.pop(0)
    point = [int(matrixInfo[2]), int(matrixInfo[3])]
    s = set()
    for direction in input():
        s.add(tuple(point))
        if direction == "S":
            point[0] += 1
            while (point[0], point[1]) in s:
                s.add(tuple(point))
                point[0] += 1
            s.add(tuple(point))
        elif direction == "E":
            point[1] += 1
            while (point[0], point[1]) in s:
                s.add(tuple(point))
                point[1] += 1
            s.add(tuple(point))
        elif direction == "N":
            point[0] -= 1
            while (point[0], point[1]) in s:
                s.add(tuple(point))
                point[0] -= 1
            s.add(tuple(point))
        else:
            point[1] -= 1
            while (point[0], point[1]) in s:
                s.add(tuple(point))
                point[1] -= 1
            s.add(tuple(point))
    print(f"Case #{case+1}: {point[0]} {point[1]}")