import math

# string = "haveaniceday"
# string = "feedthedog"
string = "chillout"

length = len(string)

rows = math.floor(math.sqrt(length))
cols = math.ceil(math.sqrt(length))

if (rows * cols < length):
    rows = cols = max(rows, cols)

print(cols)
arr = [[0 for x in range(cols)] for y in range(rows)]

count = 0
flag = 0
for i in range(rows):
    for j in range(cols):

        arr[i][j] = string[count]
        count += 1
        if (count == length):
            flag = 1
            break
    if (flag == 1):
        break

print(arr)
str1 = ""
for i in range(cols):
    for j in range(rows):
        if (arr[j][i]) != 0:
            str1 += str(arr[j][i])
    str1 += " "

print(str1)
