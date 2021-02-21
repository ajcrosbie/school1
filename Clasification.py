farm = ["horse", "cow", "sheep", "pig"]
feline = ["cat", "lion", "tiger"]
aquatic = ["whale", "dolphin", "seal", "penguin", "octopus", "squid"]
bird = ["sparrow", "ostrich"]
insect = ["spider", "ant", "bee", "wasp", "termite"]
answers = [farm, feline, aquatic, bird, insect, "dog"]

for i in answers:
    if i != "dog":
        for g in i:
            t = input(f"is it a {g}? ")
            if t == "y":
                print(f"your animal is a {g}")
    else:
        t = input(f"is it a {i}? ")
        if t == "y":
            print(f"your animal is a {i}")
        else:
            print("your animal is't in the data base")
