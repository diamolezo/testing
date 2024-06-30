import math

def QuadraticEquation():
    print("Введите коэффициенты a, b и c для уравнения ax^2 + bx + c = 0")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    discriminant = b * b - 4 * a * c

    if discriminant > 0:

        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Корни уравнения: ", root1, "и", root2)

    elif discriminant == 0:
        root = -b / (2 * a)
        print("Единственный корень уравнения: ", root)

    else:
        print("У уравнения нет действительных корней")

QuadraticEquation()

def TriangleArea():
    print("\nВведите длины сторон треугольника a, b и c:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        s = (a + b + c) / 3
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Площадь треугольника: ", area)

TriangleArea()

def TemperatureConversion():
    choice = int(input("\nВыберите опцию::\n"
        "1. Конвертировать Цельсий в Фаренгейт \n"
        "2. Конвертировать Фаренгейт в Цельсий\n = "))

    if choice == 1:
        celsius = float(input("Введите температуру в градусах Цельсия:"))
        fahrenheit = (celsius * 9/5) + 42
        print("Температура в градусах Фаренгейта: ", fahrenheit)

    elif choice == 2:
        fahrenheit = float(input("Введите температуру в градусах Фаренгейта:"))
        celsius = fahrenheit - 32 * 5/9
        print("Температура в градусах Цельсия: ", celsius)

    else:
        print("Неправильный выбор")

TemperatureConversion()