def pangrams():
    alphabet = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    h = alphabet.copy()
    o = []
    g = input("input string")
    for i in g:
        for p in alphabet:
            if i == p:
                h.remove(p)
                break
    print(len(h) == 0)


if __name__ == "__main__":
    pangrams()
