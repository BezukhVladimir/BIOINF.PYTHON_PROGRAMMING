figure = input()
if (figure == 'треугольник'):
    a, b, c = int(input()), int(input()), int(input())
    p = float((a + b + c) / 2)
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif (figure == 'прямоугольник'):
    a, b = int(input()), int(input())
    print(a * b)
elif (figure == 'круг'):
    r = int(input())
    print(3.14 * r * r)