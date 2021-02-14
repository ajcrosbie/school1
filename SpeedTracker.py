def Tracker(speed, nplate, valid):
    with open("cars.txt", "a") as f:
        f.write(f"{nplate} was traveling at {speed} m/h ")
        f.write(f"it's plate was {valid}")
        f.write("\n")


def validate(nplate):
    g = True
    try:
        for i in range(len(nplate)):
            try:
                if i == 2 or i == 3:
                    i = 4
                int(nplate[i])
                g = False
            except:
                pass

        int(nplate[2])
        int(nplate[3])
        if not g:
            return "invalid"
        else:
            return "valid"
    except:
        return "invalid "


def speedC(time1, time2, distance, nplate):
    speed = distance/(time2-time1)
    valid = validate(nplate)
    if speed > 60:
        Tracker(speed, nplate, valid)


def main():
    time1 = float(input("time passing speed camera 1 in hours "))
    time2 = float(input("time passing speed camera 2 in hours "))
    distance = float(input("distance between camera 1 and 2 in miles "))
    nplate = input("what number plate ")
    speedC(time1, time2, distance, nplate)


main()
