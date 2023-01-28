# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.

input_ = [int(i) for i in input().split()]
output_ = []
input_.sort()
for i in range(1, len(input_)):
    if input_[i] == input_[i - 1]:
        output_.append(input_[i])
print(*set(output_), end = ' ') 