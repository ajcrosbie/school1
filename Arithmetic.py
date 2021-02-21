import random


def questions():
    score = 0
    symbols = ['+', '-', '*', '/']
    for i in range(10):
        f = random.randrange(10)
        s = symbols[random.randrange(len(symbols))]
        o = random.randrange(10)
        a = int(input((f, s, o)))
        if s == '+':
            if a == f + o:
                score = score + 1
        if s == '-':
            if a == f - o:
                score = score + 1
        if s == '*':
            if a == f * o:
                score = score + 1
        if s == '/':
            if a == f / o:
                score = score + 1
    name = input("what is your name")
    W(name, score)


def W(name, score):
    with open("class.txt", "a") as f:
        f.write(name, score)


questions()
