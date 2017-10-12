def solution(A, B, K):
    # write your code in Python 2.7
    
    if A==B:
        if A%K==0:
            return 1
        else:
            return 0
    
    cnt = 0
    if A%K == 0:
        cnt +=1
    
    if A - A%K + K > B:
        return cnt
    else:
        first_in = A - A%K + K
        interval = B - first_in
        rem_int = interval%K
        cnt += (interval-rem_int)/K + 1 
        return cnt