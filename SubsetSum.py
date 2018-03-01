import sys

def SubsetSum(a, n_i):
    
    a_sum = sum(a)

    if a_sum % 2 == 1:
        return False
    
    else:
        
        #Sum of the subsequence
        ts = int(a_sum/2)
        
        # Derine the boundaries of possible summations
        # A <= s <= B
        
        a.sort()        
        A = 0
        B = 0
        
        for j in range(len(a)):
            if a[j] < 0:
                A += a[j]
            else:
                B += a[j]
        if ts < A or ts > B:
            return False
        
        n_s = abs(A) + B + 1
        
        #Now define the table for the DP aplgorithm
        d = [[0] * n_s for i in range(n_i)]
        
        for i in range(n_i):
            for s in range(n_s):
                if i == 0:
                    if a[i] == s:
                        d[i][s] = True
                    else:
                        d[i][s] = False
                else:
                    if d[i-1][s] == True or a[i] == s or d[i-1][s-a[i]] == True:
                        d[i][s] = True
                    else:
                        d[i][s] = False
    
    return d[n_i-1][ts]

n = int(input().strip())
for i in range(n):
    m = int(input().strip())
    a = [ int(num) for num in input().strip().split(" ")]
    if SubsetSum(a, m) == True:
        print("YES")
    else:
        print("NO")