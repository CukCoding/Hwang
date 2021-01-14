import sys
n = int(input())
sequence = []
result = []
stack = []
progress = 1
stc = -1
seqnum = 0
NoJudge = []
NoJudgeCopy = []
for i in range(n) :
    sequence.append(int(input()))
for j in range(n):
    for k in range(j,n):
        if sequence[j] > sequence[k] :
            NoJudge.append(sequence[k])
            NoJudgeCopy.append(sequence[k])
    NoJudge.sort()
    NoJudge.reverse()
    if NoJudge != NoJudgeCopy : 
        print('NO')
        sys.exit()
    else: 
        NoJudge = []
        NoJudgeCopy = []
while sequence != result:
    if progress <= sequence[seqnum]:
        stack.append(progress)
        stc += 1
        progress += 1
        print('+')
    if stack[stc] == sequence[seqnum]:
        print('-')
        result.append(sequence[seqnum])
        stack.pop()
        stc -= 1
        seqnum += 1