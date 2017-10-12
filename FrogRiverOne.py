from collections import Counter

def solution(X, A):
    # write your code in Python 2.7
    cnt = [0] * X
    sum_cnt = 0
    
    for i in range(len(A)):
        if cnt[A[i]-1] == 0:
            sum_cnt+= 1
            cnt[A[i]-1] = 1
        
        if sum_cnt == X:
            return i
    
    return -1