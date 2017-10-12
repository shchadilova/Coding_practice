def solution(A):
    

    
    num_right_movers = 0
    num_left_movers = 0
    
    for i in range(0,len(A)):
        if A[i]==0:
            num_right_movers += 1
        else:
            num_left_movers += num_right_movers
    
    if num_left_movers >  1000000000:
        return -1
    else:
        return num_left_movers
            