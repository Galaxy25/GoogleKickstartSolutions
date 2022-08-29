for i in range(int(input())):
    kids = int(input().split(" ")[-1])
    candies = input().split()
    candies = sum([int(u) for u in candies])
    print(f"Case #{i+1}: {candies % kids}")