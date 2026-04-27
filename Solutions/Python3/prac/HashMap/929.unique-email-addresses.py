#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        
        for email in emails:
            local, domain = email.split("@", 1)
            local = local.split("+", 1)[0].replace(".", "")
            result.add(local + "@" + domain)

        return len(result)
# @lc code=end

