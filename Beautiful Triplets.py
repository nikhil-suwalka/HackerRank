n, k = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

arr.sort()

count = 0
for i in range(len(arr) - 2):
    if ((arr[i]+k) in arr and (arr[i]+k+k) in arr):
        count += 1

print(count)