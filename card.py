from sys import stdin
import collections
n=int(stdin.readline())
array = collections.deque([i for i in range(1, n+1)])
while len(array) > 1 :
    del array[0]
    array.append(array[0])
    del array[0]

print(array[0])

