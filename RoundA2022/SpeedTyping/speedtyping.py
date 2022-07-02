cases = int(input())
for case in range(1, cases + 1):
    correct = input()
    incorrect = input()
    delete = 0
    i = 0
    u = 0
    while u < len(incorrect) and i < len(correct):
        if correct[i] == incorrect[u]:
            i += 1
            u += 1
        else:
            u += 1
            delete += 1
    if len(correct) != i:
        print(f"Case #{case}: IMPOSSIBLE")
    else:
        print(f"Case #{case}: {delete + (len(incorrect) - u)}")
