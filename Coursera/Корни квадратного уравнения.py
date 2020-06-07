print("\n**Программа для определения корней квадратного уравнения**\n")

while True:
    try:
        print("Введите коэффициенты (либо пустой ввод для выхода из программы)\n")

        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))

        print("\n...вывод результатов:\n")

        print("x1 = ", (- b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))
        print("x2 = ", (- b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), "\n\n")

    except:
        break
