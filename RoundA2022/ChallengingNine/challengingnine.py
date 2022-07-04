cases = input()

for i in range(1, int(cases) + 1):
    number = input()
    divisor = 9 - (int(number) % 9)
    number = number[::-1]
    u = 0
    end = True
    while u < len(number) and end:
        if divisor >= int(number[u]):
            number = number[:u] + str(divisor) + number[u:]
            end = False
        u += 1
    if end:
        number = number + str(divisor)
    print(f"Case #{i}: {number[::-1]}")
