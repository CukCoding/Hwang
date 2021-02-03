from sys import stdin
import math

Hnum, R = stdin.readline().split()
Hnum = int(Hnum)
R = int(R)
H = []
for i in range(Hnum):
    H.append(int(stdin.readline()))

H.sort()

total = H[-1] - H[0]
gap = 1
result = 0

while(gap <= total):
    median = math.trunc((gap + total) / 2)
    count = 1
    start = H[0]
    for i in range(1, Hnum):
        if H[i] >= start + median:
            start = H[i]
            count += 1
    if count >= R:
        gap = median + 1
        result = median
    else:
        total = median -1

print(result)

