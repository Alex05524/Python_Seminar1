def inpCoordinates(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                num = float(input(f"Введите {i+1} координату: "))
                a[i] = num
                is_OK = True
                if a[i] == 0:
                    is_OK = False
            except ValueError:
                print("Ошибка")
    return a


def checkCoordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"{text}")


coordinates = inpCoordinates(2)
checkCoordinates(coordinates)