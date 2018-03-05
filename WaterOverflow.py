# Water Overflow

import sys
import math

def Overflow(K,i, j, _cashe={}):
    
    memokey = str((K,i,j))
    
    if memokey in _cashe.keys():
        return _cashe[memokey]
    

    if j < 1 or j > i:
        return (0,0)
    else:
        
        if i == 1:
            _cashe[memokey] = activation(K)
            #print(_cashe)
            return _cashe[memokey]
        else:
            _cashe[memokey] = activation(Overflow( K, i - 1, j - 1)[1]/2 + Overflow( K , i - 1, j)[1]/2)
            #print(_cashe)
            return _cashe[memokey]
        
def activation(x):
    if x <=1:
        return [x, 0]
    else:
        return [1, x-1]

T = int(input().strip())
for t in range(T):
    K = int(input().strip())
    i = int(input().strip())
    j = int(input().strip())
    print("%.6f" %Overflow(K,i,j)[0])
    
    