# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

from collections import Counter

def solution(A):
    # write your code in Python 2.7
    
    cnt = Counter()
    
    for a in A:
        cnt[a] +=1
    #print(cnt)
    
    for i in range(1,len(A)+1):
        if cnt[i] != 1:
            return 0
    
    return 1