n = 7

# cloud = [int(x) for x in "0 0 1 0 0 1 0".split()]
# cloud = [int(x) for x in "0 0 0 0 1 0".split()]
cloud = [int(x) for x in "0 0 1 0 0 0 0 1 0 0".split()]  # 6

jumps = 0
i = 0

while (i < len(cloud) - 1):
    if (cloud[i + 1] == 0):
        jumps += 1
        if (cloud[i + 1] == 0 and cloud[i] != 1):
            i += 1
    i += 1
print(jumps)
