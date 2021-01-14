n = int(input())
start = []
end = []
result = []
count = 1

for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    start.append(a)
    end.append(b)

for i in range(0, n-1):
    for j in range(0, n-1):
        if end[j] > end[j+1]:
            endcopy = end[j]
            end[j] = end[j+1]
            end[j+1] = endcopy
            startcopy = start[j]
            start[j] = start[j+1]
            start[j+1] = startcopy

for i in range(0, n):
    for j in range(i, n-1):
        if end[i] <= start[j+1]:
            count += 1
            end[i] = end[j+1]
    result.append(count)
    count = 1

result.sort()
result.reverse()
print(result[0])

