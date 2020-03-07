#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (56.06%)
# Likes:    499
# Dislikes: 347
# Total Accepted:    173.4K
# Total Submissions: 309.1K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# Given a binary array, find the maximum number of consecutive 1s in this
# array.
# 
# Example 1:
# 
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s.
# ⁠   The maximum number of consecutive 1s is 3.
# 
# 
# 
# Note:
# 
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,max_count = 0,0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count += num
                if count > max_count:
                    max_count = count
            # print(num, count,max_count)
        return max_count
# @lc code=end

