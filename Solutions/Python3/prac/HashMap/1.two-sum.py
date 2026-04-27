
#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = {}
        
        for i, num in enumerate(nums):
            d = target - num
            
            if d in l:
                return [l[d], i]
            else:
                l[num] = i
# @lc code=end

