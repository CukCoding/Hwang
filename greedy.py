from sys import stdin

n = int(stdin.readline())
result = []
count = 1

time = [list(map(int, stdin.readline().split())) for _ in range(n)]

time= sorted(time, key = lambda x : x[0])
time= sorted(time, key = lambda x : x[1])

for i in range(0, n-1):
    if time[0][1] <= time[i+1][0]:
        time[0][1] = time[i+1][1]
        count += 1

print(count)

