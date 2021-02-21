def pin():
    nums = []
    prevs = []
    for i in range(4):
        nums.append(int(input("what is posible number?")))
    nums1 = nums.copy()
    for i in range(4):
        g = nums[i]
        for h in range(4):
            y = nums[h]
            if h == i:
                h = h+1
                if h > 3:
                    h = 0
                y = nums[h]
            for j in range(4):
                t = nums[j]
                p = True
                while p:
                    if j == i or j == h:
                        j = j+1
                        if j > 3:
                            j = 0
                        t = nums[j]
                    else:
                        p = False

                for o in range(4):
                    r = nums[o]
                    p = True
                    while p:
                        if o == i or o == h or o == j:
                            o = o+1
                            if o > 3:
                                o = 0
                            r = nums[o]
                        else:
                            p = False
                    if [g, y, t, r] in prevs:
                        pass
                    else:
                        print(g, y, t, r)
                        prevs.append([g, y, t, r])


if __name__ == "__main__":
    pin()
