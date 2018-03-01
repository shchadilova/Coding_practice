import sys

def SubsetSum(a, i , n_i, sum, _cashe={}):
        
        memokey = str((i+1,sum))
        
        if memokey in _cashe.keys():
            return _cashe[memokey]
        else:
            if sum < 0 or i>=n_i:
                return False
            elif sum == 0:
                return True
            elif a[i] == sum:
                return True
            elif SubsetSum(a,i+1,n_i,sum) == True:
                return True
            elif SubsetSum(a,i+1,n_i,sum-a[i]) == True:
                return True
            else:
                return False
    

n = int(input().strip())
for i in range(n):
    m = int(input().strip())
    a = [ int(num) for num in input().strip().split(" ")]
    if sum(a) % 2 == 1:
        print("NO")
    else:
        if SubsetSum(a, 0 , m , sum(a)/2) == True:
            print("YES")
        else:
            print("NO")

