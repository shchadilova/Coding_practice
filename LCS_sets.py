import sys

def LCS_sets(a, b):
    
    n_a = len(a) + 1
    n_b = len(b) + 1 
        
    C = [[0] * n_b for i in range(n_a)]
    
    R = {}
    
    
    for i in range(n_a):
        for j in range(n_b):
            if i == 0 or j ==0:
                R[(i,j)] = set([""])
            else:
                R[(i,j)] = set([""])
                if a[i-1] == b[j-1]:
                    C[i][j] = C[i-1][j-1] + 1
                    R[(i,j)] =  { Z + a[i-1] for Z in R[(i-1,j-1)] }
                else:
                    if C[i-1][j] >= C[i][j-1]:
                        C[i][j] = C[i-1][j]
                        R[(i,j)] = R[(i,j)].union(R[(i-1,j)])
                    if C[i][j-1] >= C[i-1][j]:
                        C[i][j] = C[i][j-1]
                        R[(i,j)] = R[(i,j)].union(R[(i,j-1)])
                    
    return (C[-1][-1], R[(n_a-1,n_b-1)] )
    


T = int(input().strip())
for t in range(T):
    a, b = input().strip().split(' ')
    d, R = LCS_sets(a,b)
    R_d = []
    for e in R:
        if len(e) == d:
            R_d = R_d + [e]
    R_d.sort()
    print(" ".join(str(e) for e in R_d))
