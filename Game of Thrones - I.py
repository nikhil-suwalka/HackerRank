str = input()

dic = {}

for i in str:
    if (i in dic):
        dic[i] += 1
    else:
        dic[i] = 1

odds = 0
for i in dic:
    if (dic[i] % 2 == 1):
        odds += 1

if (odds <= 1):
    print("YES")
else:
    print("NO")
