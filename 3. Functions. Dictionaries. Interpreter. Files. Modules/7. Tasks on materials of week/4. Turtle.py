# Вас просят написать программу, которая выведет точку, в которой окажется черепашка после всех команд.

N = int(input())
route = ""
amount = 0
x = 0
y = 0
for i in range(N):
    route, amount = [int(i) if i.isdigit() else i for i in input().split()]
    if "север" == route:
        y += amount                
    if "юг" == route:
        y -= amount        
    if "запад" == route:
        x -= amount
    if "восток" == route:
        x += amount
        
print(x, y)