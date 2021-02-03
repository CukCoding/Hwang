A = int( input () )
for i in range(1, A+1):
    
        for j in range(1, A-i+1):

            print(' ',end='')

        for j in range(1,i+1):

            if j!=i : print('*',end='')

            else : 
             print('*')

            
    
