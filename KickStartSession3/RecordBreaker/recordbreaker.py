for i in range(int(input())):
    input()
    prev = -1
    records = 0
    days = input().split()
    days = [int(u) for u in days]
    for u in range(len(days)-1):
        if prev < days[u] and days[u] > days[u+1]:
            records += 1
        prev = max(days[u], prev)
    if prev < days[-1]:
        records += 1
    print(f"Case #{i+1}: {records}")