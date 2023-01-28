l = [int(i) for i in input().split()]
x = int(input())
is_not_found = True
for i in range(len(l)):
    if l[i] == x:
        print(i, end = ' ')
        is_not_found = False
if is_not_found:
    print('Отсутствует', end = ' ')