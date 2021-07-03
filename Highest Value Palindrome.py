# https://www.hackerrank.com/challenges/richie-rich

def is_palindrome(num: list):
    return num == num[::-1]


n, k = map(int, input().split())
num = [x for x in input()]

changed = [0 for _ in range(n // 2 + 1)]

# Make the number palindrome first by changing the digits less than k
if not is_palindrome(num):
    i = n // 2
    while k > 0 and i < n:
        if num[i] != num[n - 1 - i]:
            if num[i] >= num[n - 1 - i]:
                num[n - 1 - i] = num[i]
            else:
                num[i] = num[n - 1 - i]
            changed[n - 1 - i] = 1
            k -= 1
        i += 1

# If still not palindrome then return -1
if not is_palindrome(num):
    print(-1)

# Make the number largest by changing upto k digits
else:
    i = 0
    while k > 0 and i < n // 2:

        # If both already 9 then skip
        if min(num[i], num[n - 1 - i]) != "9":

            # If both digits can be changed (k>=2) or one of the digit is changed previously (so can be made 9 without reducing k)
            if k >= 2 or changed[i] == 1:
                num[i], num[n - 1 - i] = "9", "9"
                k = k - 1 if changed[i] == 1 else k - 2

            # If the numbers are not same then make both to highest of the two.
            elif (num[i] != num[n - 1 - i]) :
                m = max(num[i], num[n - 1 - i])
                num[i], num[n - 1 - i] = m, m
                k -= 1
        i += 1

    # If n is odd and k > 0  then make middle one to 9.
    if k > 0 and n % 2 != 0:
        num[n // 2] = "9"

    print("".join(num))
