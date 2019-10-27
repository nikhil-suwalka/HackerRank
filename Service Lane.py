n, t = [int(x) for x in input().split()]
widths = [int(x) for x in input().split()]

for _ in range(t):
    a, b = [int(x) for x in input().split()]

    print(min(widths[a:b + 1]))
