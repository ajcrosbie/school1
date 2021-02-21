import random


def roll(money):
    symbols = ["cherry", "bell", "lemon", "Orange", "Star", "Skull", "Skull"]
    end = []
    for i in range(3):
        end.append(symbols[random.randrange(len(symbols))])
    print(end)
    return outcome(end, money)


def outcome(end, money):
    if end[0] == "Skull" and end[1] == "Skull":
        money = money - 1
    elif end[0] == "Skull" and end[2] == "Skull":
        money = money - 1
    elif end[1] == "Skull" and end[2] == "Skull":
        money = money - 1
    elif end[0] == end[1] and end[1] == end[2] and end[2] == "Skull":
        money = 0
    elif end[0] == end[1] and end[1] == end[2] and end[2] == "Bell":
        money = money + 5
    elif end[0] == end[1] and end[0] == end[2]:
        money = money + 1
    elif end[0] == end[1] or end[0] == end[2] or end[1] == end[2]:
        money = money + 0.5
    return money


def menu():
    money = 1
    while True:
        print("you have ", money, "pounds")
        if money < 0:
            print("no money left you lose")
            quit()
        v = input("roll again? ")
        if v == "y":
            money = roll(money)
        else:
            print(f"you now have {money} pounds")
            quit()


if __name__ == "__main__":
    menu()
