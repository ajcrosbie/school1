def findFactLoop(n):
    answer = 1
    while n > 0:
        answer = answer*n
        n = n - 1
    return answer


def findFactRecursive(n):
    if n == 1:
        return 1
    else:
        return n*findFactRecursive(n-1)


n = int(input("whole number? "))
print("0 for a loop method")
m = int(input("1 for a recursive method, anything else to leave "))
if m == 0:
    print(findFactLoop(n))
elif m == 1:
    print(findFactRecursive(n))
