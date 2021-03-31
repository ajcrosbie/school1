import random


def cipher():
    alphabet = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    n = random.randrange(0, 26)
    out = []
    g = {}
    J = input("stuff")
    for i in J:
        t = 0
        for g in alphabet:
            if g == i:
                break
            t = t + 1
        h = t+n
        if h > 25:
            h = h - 26
        out.append(alphabet[h])
    print(out)


if __name__ == "__main__":
    cipher()
