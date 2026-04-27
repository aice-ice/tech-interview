#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                l.append(i)
            elif i == ")" and l and l[-1] == "(":
                l.pop()
            elif i == "}" and l and l[-1] == "{":
                l.pop()
            elif i == "]" and l  and l[-1] == "[":
                l.pop()
            else:
                return False
        
        return  not l
        
# @lc code=end

