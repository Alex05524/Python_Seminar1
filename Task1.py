def Numbers(inpText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inpText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def chckNum(numb):
    if 6 <= numb <= 7:
        print("Да")
    elif 0 < numb < 6:
        print("Нет")


numb = Numbers("Введите число: ")
chckNum(numb)