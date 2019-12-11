n = int(input())
s = input()
k = int(input())

if(k > 26):
    k%=26
res = ""
for i in s:
    if (ord(i) >= 97 and ord(i) <= 122):
        if (ord(i) + k > 122):
            res += chr(97 - (122 - ord(i)) + k - 1)
        else:
            res += chr(ord(i) + k)
    elif(ord(i) >= 65 and ord(i) <= 90):
        if (ord(i) + k > 90):
            res += chr(65 - (90 - ord(i)) + k - 1)
        else:
            res += chr(ord(i) + k)

    else:
        res += i

print(res)
