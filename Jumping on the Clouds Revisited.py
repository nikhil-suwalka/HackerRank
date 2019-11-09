n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
e = 100
curr = 0
while True:
    curr = (curr + k) % n
    if (arr[curr] == 1):
        e -= 3
    else:
        e -= 1
    if (curr == 0):
        break
print(e)
