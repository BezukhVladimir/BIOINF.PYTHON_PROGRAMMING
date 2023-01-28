# Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.

zero_check = int(input())
summa = zero_check ** 2
while (zero_check):
    tmp = int(input())
    summa += tmp ** 2
    zero_check += tmp
print(summa)