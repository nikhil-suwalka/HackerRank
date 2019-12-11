for _ in range(int(input())):
    s = " " + input()
    flag = 0
    for i in "hackerrank":
        if (s.find(i) == -1):
            flag = 2
            break
        else:
            s = s[s.find(i) + 1:]

    if (flag == 2):
        print("NO")
    else:
        print("YES")
