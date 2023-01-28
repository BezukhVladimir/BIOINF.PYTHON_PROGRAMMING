# Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n = 5)

N = int(input())
m = [[0] * N for i in range(N)]
count_loop = 0
count = 0
while(count < N ** 2):
    count_loop += 1
    for i in range(count_loop - 1, N - count_loop + 1):
        count += 1
        m[count_loop - 1][i] = count
    if (count < N ** 2):
        for i in range(count_loop, N - count_loop + 1):
            count += 1
            m[i][N - count_loop] = count
    if (count < N ** 2):
        for i in range(count_loop, N - count_loop + 1):
            count += 1
            m[N - count_loop][N - i - 1] = count
    if (count < N ** 2):
        for i in range(count_loop, N - count_loop):
            count += 1
            m[N - i - 1][count_loop - 1] = count
for i in range(N):
    for j in range(N):
        print(m[i][j], end = ' ')
    print('\n', end = '')