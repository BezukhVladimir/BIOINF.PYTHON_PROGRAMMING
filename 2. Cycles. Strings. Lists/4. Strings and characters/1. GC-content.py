# Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).

string = input()
count = 0
for N in string:
    if (N == 'C' or
        N == 'c' or
        N == 'G' or
        N == 'g'):
        count += 1
print(count * 100 / len(String))