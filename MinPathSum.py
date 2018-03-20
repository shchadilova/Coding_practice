class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_rows = len(grid)
        num_col = len(grid[0])
        
        _cache = {}
        return Solution.minPathSum_step(self,grid, 0, 0, num_col,num_rows, _cache)
        
    def minPathSum_step(self, grid, i , j, num_col , num_rows, _cache={}):
        
        memo = str((i,j))
        
        if memo in _cache.keys():
            return _cache[memo]
        
        
        if i == num_col-1:
            cost = 0
            for j_cur in range(j,num_rows):
                cost += grid[j_cur][i]
            _cache[memo] = cost
            return cost
        elif j == num_rows-1:
            cost = 0
            for i_cur in range(i,num_col):
                cost += grid[j][i_cur]
            _cache[memo] = cost
            return cost
        else:
            _cache[memo] = grid[j][i] + min( Solution.minPathSum_step(self, grid, i+1 ,j , num_col,num_rows,_cache), Solution.minPathSum_step(self, grid, i , j +1 , num_col,num_rows,_cache) )
            return _cache[memo]
        

        
        
        
        