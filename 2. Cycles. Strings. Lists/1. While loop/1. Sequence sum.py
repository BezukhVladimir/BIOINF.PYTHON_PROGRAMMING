# Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.

N = int(input())
SUMMA = 0
while (N):
    SUMMA += N
    N = int(input())
print(SUMMA)