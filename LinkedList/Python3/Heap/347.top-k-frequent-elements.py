#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import heapq
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        
        return [x for x, _ in heapq.nlargest(k, c.items(), key=lambda item: item[1])]
    
# @lc code=end

