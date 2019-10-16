def getCommon(l1, l2):
    c = 0
    for i in l1:
        if (i in l2):
            c += 1
            l2.remove(i)
    return c


str1 = [x for x in input()]
str2 = [x for x in input()]

common = getCommon(str1.copy(), str2.copy())
print((len(str1) - common) + (len(str2) - common))