def inpNums(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                num = int(input(f"Введите координату по {xy[i]}: "))
                a.append(num)
                is_OK = True
            except ValueError:
                print("Ошибка! Введите целое число!")
    return a


def Distance(a, b):
    distance = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return distance


print("Введите А")
A = inpNums(2)
print("Введите В")
B = inpNums(2)

print(f"{format(Distance(A, B), '.2f')}")