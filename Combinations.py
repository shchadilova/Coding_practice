import sys

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        return Solution.combine_set(self,n,k)

    def combine_set(self,n,k):
        
        if k == n:
            t=[]
            for i in range(1,n+1):
                t= t + [i]
            return [t]  
        elif k == 0:
            return [[]]
        else:
            return Solution.combine_set(self,n-1,k) + [ Z + [n] for Z in Solution.combine_set(self, n-1,k-1) ]
        
        

        
        
        