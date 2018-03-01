#Longest Increasing Subsequence
import sys

def LIS(arr,m):
    length_of_sequence = [1]*m
    
    for i in range( 1, m):
        for j in range(i):
            if arr[j]<arr[i]:
                length_of_sequence[i] = max(length_of_sequence[j] + 1,length_of_sequence[i])
    return max(length_of_sequence)        

n = int(input().strip())
for i in range(n):
    m = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ') ]
    print(LIS(arr,m)
