def solve(year):
    if (year <= 1917):
        if (year % 4 == 0):
            str1 = "12.09." + str(year)
        else:
            str1 = "13.09." + str(year)
    elif(year == 1918):
            str1="26.09.1918"
    else:
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            str1 = "12.09." + str(year)
        else:
            str1 = "13.09." + str(year)
    return str1


print(solve(2017))
