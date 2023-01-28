A, B, op = float(input()), float(input()), input()
if (op == '+'):
    print(A + B)
if (op == '-'):
    print(A - B)
if (op == '/'):
    if (B):
        print(A / B)
    else:
        print("Деление на 0!")
if (op == '*'):
    print(A * B)
if (op == 'mod'):
    if (B):
        print(A % B)
    else:
        print("Деление на 0!")
if (op == 'pow'):
    print(A ** B)
if (op == 'div'):
    if (B):
        print(A // B)
    else:
        print("Деление на 0!")