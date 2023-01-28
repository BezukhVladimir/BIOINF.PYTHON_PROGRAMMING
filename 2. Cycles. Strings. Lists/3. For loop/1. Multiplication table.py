# Программа должна вывести фрагмент таблицы умножения.

A, B, C, D = int(input()), int(input()), int(input()), int(input())
Tab = "\t"
print(Tab.join(str(i) for i in range(C, D + 1)))
for i in range(A, B + 1):
    print(i, Tab.join(str(i * j) for j in range(C, D + 1)))