import math

A, B= input().split()
A = int(A)
B = int(B)
div = math.trunc(A/B)
print(A+B)
print(A-B)
print(A*B)
print(div)
print(A%B)