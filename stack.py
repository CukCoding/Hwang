import sys
n = int(input())
sequence = []
result = []
stack = []
progress = 1
stc = -1
sign = []

for i in range(n) :
    sequence.append(int(input()))

for i in range(0,n):
    while progress <= sequence[i]:
        stack.append(progress)
        stc += 1
        progress += 1
        sign.append('+')
    if stack[stc] == sequence[i]:
        sign.append('-')
        result.append(sequence[i])
        stack.pop()
        stc -= 1
    else : 
        print('NO')
        exit()

for j in sign :
    print(j)
        