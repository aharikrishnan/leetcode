#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (41.86%)
# Likes:    3725
# Dislikes: 84
# Total Accepted:    315.5K
# Total Submissions: 752.8K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#

# @lc code=start
import heapq
# from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seen = []
        for num in nums:
            nums_lt_count = self.floorSearch(seen, num)+1
            if nums_lt_count == len(seen):
                seen.append(num)
            else:
                seen[nums_lt_count] = num
            # print(seen, num, nums_lt_count)
        return len(seen)
    
    def floorSearch(self, arr, x):
        start, end = 0, len(arr)-1
        floor = -1
        while start <= end:
            mid = (start + end)//2
            if arr[mid] < x:
                floor = mid
                start = mid + 1
            else:
                end = mid - 1
        return floor




# @lc code=end

