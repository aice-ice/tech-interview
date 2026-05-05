#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        s = list(s)
        result = -1


        for i, m in enumerate(s[1:]):
            if m not in s[1:]:
                result = i
                break
                
            
        
        return result        
# @lc code=end

