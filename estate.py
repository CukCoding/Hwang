N = input().split()
countArray = []
Arraycount = 0
estateNum = 1
count = 0
array = [list(map(int, input())) for _ in range(N)]
temprow = 0
tempcol = 0
rowstart = 0
colstart = 0
for rowcount in range(N) :
    for colcount in range(N) :
        if array[rowcount][colcount] == 1 :
            array[rowcount][colcount] = 0
            temprow = rowcount
            tempcol = colcount
            rowstart = rowcount
            colstart = colcount
            while count >= N*N :
                    if array[temprow][tempcol+1] == 1 :
                        array[temprow][tempcol+1] = 0
                        tempcol += 1
                        count += 1
                    else : 
                        if array[temprow+1][tempcol] == 1 :
                            array[temprow+1][tempcol] = 0
                            temprow += 1
                            count += 1
                        else : 
                            tempcol = colstart

