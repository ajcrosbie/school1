def happy(n):
    if n == 1:
        print("happy")
    elif n < 10:
        print(n)
        print("unhappy")
    else:
        g = 0
        for i in str(n):
            g = g + (int(i)**2)
        happy(g)


happy(12)
