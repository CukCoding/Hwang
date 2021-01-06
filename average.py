testcase = int(input())
addresult = 0
avgresult = []
count = 0
percent = []
array = [[0 for col in range(testcase)]for row in range(1000)]
for i in range(testcase) :
      array[i] = list(map(int, input().split()))
      for k in range(0,array[i][0]+1):
        if k == 0 : addresult = 0 
        else : addresult = addresult + array[i][k]
      avgresult.append(addresult/array[i][0])
      addresult = 0
      for j in range(1,array[i][0]+1):
          if array[i][j] > avgresult[i] : count = count + 100
      percent.append(count/array[i][0])
      count = 0

for j in range(testcase) : 
    print('%.3f%%' % percent[j])