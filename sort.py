n = int(input())
array = [int(input()) for _ in range(n)]
array = sorted(array)

for i in range(0,n):
    print(array[i])

print(array)