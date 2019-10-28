cases = int(input())

for _ in range(cases):
    money, cost, wrappers = [int(x) for x in input().split()]

    chocolates = money // cost
    wraps = chocolates

    while (wraps >= wrappers):
        chocolates += wraps // wrappers
        wraps = ((wraps // wrappers)) + (wraps % wrappers)
    print(chocolates)
