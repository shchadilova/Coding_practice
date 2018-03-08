import sys

def CountWays(N):
    
    
    first = 1
    second = 1
    third = 2
    fourth = 4
    
    for i in range(5, N) :
        curr = (first + second + fourth) % (10**9+7)
        first = second
        second = third
        third =  fourth
        fourth = curr
    
    return fourth 
    
T = int(input().strip())
for t in range(T):
    N = int(input().strip())
    #arr = input().strip().split(' ')
    print(CountWays(N+1))