N = int(input())
d = {}
for i in range(N):
    x = int(input())
    if x in d:
        print(d[x])      
    else:
        d[x] = f(x)
        print(d[x])