class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _cache={}
        if len(nums) == 0:
            return 0
        else:
            return max(Solution.rob_cache(self, nums, 1, 0, _cache), nums[0] + Solution.rob_cache(self, nums, 2, 1, _cache))
    
    def rob_cache(self, nums, i, first, _cache={}):
        
        memo = str((i,first))
        if memo in _cache.keys():
            return _cache[memo]
        
        if i > len(nums) - 1:
            _cache[memo]= 0
            return 0
        elif i == len(nums) - 1:
            _cache[memo] = (1-first)*nums[i]
            return (1-first)*nums[i]
        else:
            _cache[memo] = max(nums[i] + Solution.rob_cache(self, nums, i+2, first, _cache) , Solution.rob_cache(self, nums, i+1, first, _cache) )
            return _cache[memo]