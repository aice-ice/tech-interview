#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        l = []
        n = len(nums1)
        m = len(nums2)
        v = set()
        heap = [(nums1[0]+nums2[0], (0, 0))]
        
        if n == 0 or m == 0:
            return []
        
        for _ in range(min(k, n*m)):
            sum, (i, j) = heapq.heappop(heap)
            l.append([nums1[i], nums2[j]])
            
            if i+1 < n and (i+1, j) not in v:
                heapq.heappush(heap, (nums1[i+1]+nums2[j], (i+1, j)))
                v.add((i+1, j))
            if j+1 < m and (i, j+1) not in v:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], (i, j+1)))
                v.add((i, j+1))
                

        return l
# @lc code=end

