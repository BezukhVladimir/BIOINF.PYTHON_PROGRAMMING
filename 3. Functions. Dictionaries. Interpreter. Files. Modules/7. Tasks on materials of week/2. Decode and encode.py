# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.

key, value, encode, decode = input(), input(), input(), input()

for c in encode
    print(value[key.index(c)], end = )
print()
    
for c in decode
    print(key[value.index(c)], end = )
print()