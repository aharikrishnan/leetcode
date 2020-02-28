#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Medium (37.94%)
# Likes:    524
# Dislikes: 473
# Total Accepted:    154.2K
# Total Submissions: 404K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
# 
# Example 1:
# 
# 
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# 
# 
# Example 2:
# 
# 
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
# 
# 
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        sz = len(nums)
        res = []
        if sz == 0: return res

        def insertRange(start, end):
            if start == end:
                res.append(str(nums[start]))
            else:
                res.append(str(nums[start])+"->"+str(nums[end]))

        start, end = 0, 1
        while end < sz:
            if nums[end] != nums[end-1]+1:
                insertRange(start, end-1)
                start = end
            end += 1
        insertRange(start, end-1)
        return res


            
        
# @lc code=end

