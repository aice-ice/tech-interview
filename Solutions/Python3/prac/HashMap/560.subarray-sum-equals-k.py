#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_dict = {0:1}
        total = 0
        for n in nums:
            total += n
            if total - k in sum_dict:
                count += sum_dict[total - k]
            if total in sum_dict:
                sum_dict[total] += 1
            else:
                sum_dict[total] = 1
        return count
    
        
# @lc code=end
