#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (44.45%)
# Likes:    2451
# Dislikes: 191
# Total Accepted:    406.6K
# Total Submissions: 913.2K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this
# problem.
# 
# Example:
# 
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Follow up:
# 
# 
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# 
# 
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sz = len(nums)
        red, white, blue  = 0, 0, sz-1
        while white <= blue:
            if nums[white] == 0:
                nums[red],nums[white] = nums[white],nums[red]
                # print("Swapped [0]", red, white, [red, white, blue])
                red += 1
                white += 1
            elif nums[white] == 2:
                nums[blue],nums[white] = nums[white],nums[blue]
                # print("Swapped [2]", blue, white, [red, white, blue])
                blue -= 1
            elif nums[white] == 1:
                # print("No Swap Incr [1]", white, [red, white, blue])
                white += 1
        # print(nums)
# @lc code=end

