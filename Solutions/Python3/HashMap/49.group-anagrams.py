#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        
        if len(strs) == 0:
            return [strs]
        
        for i in strs:
            s = "".join(sorted(i))
            
            if s in result:
                result[s].append(i)
            else:
                result[s] = [i]
        
        return list(result.values())
# @lc code=end

