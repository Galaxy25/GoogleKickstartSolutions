from math import floor
cases = int(input())
for i in range(1, cases+1):
    categories = int(input().split(" ")[-1])

    sizes = input()
    sizes = sizes.split(" ")
    sizes = [int(a) for a in sizes if a != " "]
    sizes.sort(reverse=True)
    total = sum(sizes[:categories-1])
    sizes = sizes[categories-1:]
    if len(sizes) % 2 == 0:
        total += (sizes[len(sizes)//2 - 1] + sizes[len(sizes)//2]) / 2
    else:
        total += sizes[floor(len(sizes)/2)]
    print(f"Case #{i}: {float(total)}")