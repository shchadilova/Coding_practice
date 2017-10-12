
def solution(N, A):
    
    cnt = [0] * N
    max_counter = 0
    current_max = 0
    
    for cmnd in A:
        if cmnd <= N:
            if max_counter > cnt[cmnd-1]:
                cnt[cmnd-1] = max_counter
            cnt[cmnd-1] +=1
            if current_max < cnt[cmnd-1]:
                current_max = cnt[cmnd-1]
        else: 
            max_counter = current_max
    
    for i in range(N):
        if cnt[i] < max_counter:
            cnt[i] = max_counter
            
    return cnt