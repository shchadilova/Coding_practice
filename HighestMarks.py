import sys

def HighestMarks(marks, N , K):
    
    d = {}
    top_marks = [0]*K
    
    for i in range(N):
        if marks[i] in d.keys():
            d[marks[i]] = d[marks[i]] + [str(i)]
        else:
            d[marks[i]] = [str(i)]
            cur_top = sorted(top_marks + [marks[i]],reverse=True)
            top_marks = cur_top[0:K]
    
    answer = []
    for t in top_marks:
        answer = answer + d[t]
    
    return answer
        

T = int(input().strip())
for t in range(T):
    N = int(input().strip())
    marks = [int(m) for m in input().strip().split(' ')]
    K = int(input().strip())
    answer = HighestMarks(marks, N , K)
    print(" ".join(answer ) )