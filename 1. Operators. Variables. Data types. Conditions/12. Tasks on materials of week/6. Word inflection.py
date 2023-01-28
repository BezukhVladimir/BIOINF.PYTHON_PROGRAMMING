N = int(input())
if (N % 100 != 11 and N % 10 == 1):
    print(N, "программист")
elif (10 < N % 100 < 15
   or  4 < N % 10 < 10
   or N % 10 == 0):
    print(N, "программистов")
else:
    print(N, "программиста")