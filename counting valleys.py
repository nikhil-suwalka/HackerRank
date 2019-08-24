n = 8
# s = "UDDDUDUU"
# s = "DDUUUUDD"
s = "DDUUDDUDUUUD"  # 2
valley_count = 0
level = 0

i = 0

# s = "DDUUDDUUD"

while (i < len(s)):

    if (s[i] == "U"):
        level += 1
    else:
        level -= 1
    i += 1

    if (level < 0):
        valley_count += 1
        while (level != 0 and i < len(s)):
            if (s[i] == "U"):
                level += 1
            else:
                level -= 1
            i += 1

print(valley_count)
