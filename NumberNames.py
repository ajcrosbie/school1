g = int(input("number "))
if g > 1000000:
    print("too large")
    quit()
if g < 0:
    print("too small")
    quit()
if g > 100000:
    if g // 100000 == 9:
        g = g - 900000
        if g // 10000 == 90000:
            if g - 90000 // 1000 == 9000:
                print('nine-hundred and ninety nine thousand')
            if g - 90000 // 1000 == 8000:
                print('nine-hundred and ninety eight thousand')
            if g - 90000 // 1000 == 7000:
                print('nine-hundred and ninety seven thousand')
            if g - 90000 // 1000 == 6000:
                print('nine-hundred and ninety six thousand')
            if g - 90000 // 1000 == 5000:
                print('nine-hundred and ninety five thousand')
            if g - 90000 // 1000 == 4000:
                print('nine-hundred and ninety four thousand')
            if g - 90000 // 1000 == 3000:
                print('nine-hundred and ninety three thousand')
            if g - 90000 // 1000 == 2000:
                print('nine-hundred and ninety two thousand')
            if g - 90000 // 1000 == 1000:
                print('nine-hundred and ninety one thousand')
            if g - 90000 // 1000 == 0:
                print('nine-hundred and ninety thousand')
    if g // 100000 == 8:
        print("eight hundred thousand")
        g = g - 800000
    if g // 100000 == 7:
        print("seven hundred thousand")
        g = g - 700000
    if g // 100000 == 6:
        print("six hundred thousand")
        g = g - 600000
    if g // 100000 == 5:
        print("five hundred thousand")
        g = g - 500000
    if g // 100000 == 4:
        print("four hundred thousand")
        g = g - 400000
    if g // 100000 == 3:
        print("three hundred thousand")
        g = g - 300000
    if g // 100000 == 2:
        print("two hundred thousand")
        g = g - 200000
    if g // 100000 == 1:
        print("one hundred thousand")
    if g // 100000 == 0:
        print()
        g = g - 100000
if g // 10000 == 90000:
    if g - 90000 // 1000 == 9000:
        print()
    if g - 90000 // 1000 == 8000:
        pass
    if g - 90000 // 1000 == 7000:
        pass
    if g - 90000 // 1000 == 6000:
        pass
    if g - 90000 // 1000 == 5000:
        pass
    if g - 90000 // 1000 == 4000:
        pass
    if g - 90000 // 1000 == 3000:
        pass
    if g - 90000 // 1000 == 2000:
        pass
    if g - 90000 // 1000 == 1000:
        pass
