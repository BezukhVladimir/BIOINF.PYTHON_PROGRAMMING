A, B, C = int(input()), int(input()), int(input())
if (A > B):
    A, B = B, A
if (B > C):
    B, C = C, B
if (A > B):
    A, B = B, A
print(C, A, B, sep = '\n')