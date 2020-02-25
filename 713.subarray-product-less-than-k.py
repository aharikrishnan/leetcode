#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#
# https://leetcode.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (38.33%)
# Likes:    968
# Dislikes: 47
# Total Accepted:    47K
# Total Submissions: 122.5K
# Testcase Example:  '[10,5,2,6]\n100'
#
# Your are given an array of positive integers nums.
# Count and print the number of (contiguous) subarrays where the product of all
# the elements in the subarray is less than k.
# 
# Example 1:
# 
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5],
# [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly
# less than k.
# 
# 
# 
# Note:
# 0 < nums.length .
# 0 < nums[i] < 1000.
# 0 .
# 
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        sz = len(nums)
        i,j = 0,0
        ans, p1 = 0, 1
        if k <= 1: return ans
        while j < sz:
            p1 *= nums[j]
            while p1 >= k and i <= j:
                p1 /= nums[i]
                i += 1
            ans += j-i+1
            j += 1
        return ans

        
# @lc code=end

