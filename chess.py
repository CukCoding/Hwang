A, B = input().split()
A = int(A)
B = int(B)
whitecount = 0
blackcount = 0
comparison = []
array = [list(map(str, input())) for row in range(A)]
for rowrange in range(0, B-7) :
        for colrange in range(0, A-7): 
            for colcount in range(colrange,colrange+8):
                for rowcount in range(rowrange,rowrange+8):
                    if array[colcount][rowcount]=='B' and (colcount+rowcount)%2==0 :
                        whitecount+=1
                    if array[colcount][rowcount]=='W' and (colcount+rowcount)%2==1 :
                        whitecount+=1
                for rowcount in range(rowrange,rowrange+8):
                    if array[colcount][rowcount]=='W' and (colcount+rowcount)%2==0 :
                        blackcount+=1
                    if array[colcount][rowcount]=='B' and (colcount+rowcount)%2==1 :
                        blackcount+=1  
            comparison.append(whitecount)
            whitecount=0  
            comparison.append(blackcount)
            blackcount = 0
comparison.sort()
print(comparison[0])

