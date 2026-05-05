#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = collections.defaultdict(int)
        res[0] = 0
        
        def bfs(r, c, islands):
            if not 0 <= r < rows or not 0 <= c < cols or grid[r][c] != 1 or (r, c) in visited:
                return
            res[islands] += 1
            visited.add((r, c))
            bfs(r + 1, c, islands)
            bfs(r - 1, c, islands)
            bfs(r, c + 1, islands)
            bfs(r, c - 1, islands)
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c, islands)  
            
        
        return max(res.values())            

# @lc code=end

