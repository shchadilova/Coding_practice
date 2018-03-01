import sys


def SubsetSum(a, n_i , s, sum):
    
    n_s = sum + 1
    
    #Now define the table for the DP aplgorithm
    d = [[False] * n_s for i in range(n_i)]
    
    for i in range(n_i):
        for s in range(n_s):
            if i == 0:
                d[i][s] = (a[i] == s)
            else:
                d[i][s] = (d[i-1][s]) or (a[i] == s) or (d[i-1][s-a[i]])
                    
    return d[n_i-1][-1]

n = int(input().strip())
for i in range(n):
    m = int(input().strip())
    a = [ int(num) for num in input().strip().split(" ")]
    if sum(a) % 2 == 1:
        print("NO")
    else:
        if SubsetSum(a, len(a) , i , int(sum(a)/2)) == True:
            print("YES")
        else:
            print("NO")