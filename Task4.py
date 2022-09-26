print("Введите координаты:")
x = float(input("x = "))
y = float(input("y = "))

if x > 0 and y > 0:
    print("Точка находится в I четверти")
elif x < 0 and y > 0:
    print("Точка находится в II четверти")
elif x < 0 and y < 0:
    print("Точка находится в III четверти")
elif x > 0 and y < 0:
    print("Точка находится в IV четверти")