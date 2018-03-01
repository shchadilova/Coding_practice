import sys

def LCS(a, b):
    
    n_a = len(a) + 1
    n_b = len(b) + 1 
        
    d = [[0] * n_b for i in range(n_a)]
    
    for i in range(1, n_a):
        for j in range(1, n_b):
            if a[i-1] == b[j-1]:
                d[i][j] = d[i-1][j-1] + 1

            else:
                d[i][j] = max(d[i-1][j],d[i][j-1])
            
    return d[-1][-1]
    
    
n = int(input().strip())
for i in range(n):
    m1, m2 = input().strip().split(' ')
    m1, m2 = [int(m1), int(m2)]
    if m1 == 0 or m2 == 0:
        input().strip().split(' ')
        input().strip().split(' ')
        print(0)
    else:
        arr1 = list(input().strip())
        arr2 = list(input().strip())
        print(LCS(arr1, arr2))