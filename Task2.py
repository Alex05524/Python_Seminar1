def inpNum(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def chckPred(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inpNum(3)

if chckPred(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")