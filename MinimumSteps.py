import sys
import math

def MinSteps(P,X,Y, _cashe = {}):
    
    memokey = str((P,X,Y))
    
    if memokey in _cashe.keys():
        return _cashe[memokey]
    
    if P < X or X == 1:
        d_x = P
    else:
        x_pow = math.floor(math.log(P,X))
        #print("P: %d, x_pow: %d" %(P,x_pow))
        d_x = 1 + MinSteps(P - X**x_pow,X,Y)
    
    if P < Y or Y == 1:
        d_y = P
    else:
        y_pow = math.floor(math.log(P,Y))
        #print("P: %d, y_pow: %d" %(P,y_pow))
        d_y = 1 + MinSteps(P - Y**y_pow,X,Y)
    
    _cashe[memokey] = min(d_x,d_y)
    return _cashe[memokey]
        
    

T = int(input().strip())
for t in range(T):
    P, X, Y = input().strip().split(' ')
    P,X ,Y = int(P), int (X),int(Y)
    _cashe = {}
    print(MinSteps(P,X,Y))