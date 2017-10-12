def solution(S, P, Q):


    answer = ["T"] * len(P)
    answer_impact = [4] * len(P)
    
    for K in range(len(P)):
        current_el = P[K]
        while current_el < Q[K]+1:
            #print(current_el , S[current_el], answer[K])
            if S[current_el] < answer[K]:
                answer[K] = S[current_el]
            if answer[K] == "A":
                answer_impact[K] = 1
                current_el = Q[K]+1
            current_el+= 1
        
        if answer[K] == "C":
            answer_impact[K] = 2
        if answer[K] == "G":
            answer_impact[K] = 3
        if answer[K] == "T":
            answer_impact[K] = 4
    
    return answer_impact

▶ almost_all_same_letters 
GGGGGG..??..GGGGGG..??..GGGGGG ✘TIMEOUT ERROR 
running time: >6.00 sec., time limit: 0.75 sec.
▶ large_random 
large random string, length ✘TIMEOUT ERROR 
running time: >6.00 sec., time limit: 0.78 sec.
▶ extreme_large 
all max ranges ✘TIMEOUT ERROR 
running time: >6.00 sec., time limit: 0.90 sec.