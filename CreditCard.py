def makeV():
    valid = []
    for i in range(10000):
        if i < 10:
            valid.append("000" + str(i))
        elif i < 100:
            valid.append("00" + str(i))
        elif i < 1000:
            valid.append("0" + str(i))
    return valid


cNumber = input("creddit card number")
if cNumber in makeV():
    print("valid")
else:
    print("invalid")
