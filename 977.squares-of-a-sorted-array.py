#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (72.19%)
# Likes:    727
# Dislikes: 68
# Total Accepted:    149.4K
# Total Submissions: 207K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an array of integers A sorted in non-decreasing order, return an array
# of the squares of each number, also in sorted non-decreasing order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# 
# 
# 
# Example 2:
# 
# 
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.
# 
# 
# 
#

# @lc code=start

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        sz = len(A)
        i,j,k = 0, sz-1, sz-1
        ans = [None] * sz
        while i <= j:
            x,y = A[i]**2, A[j]**2
            if x > y:
                ans[k] = x
                i+=1
            else:
                ans[k] = y
                j-=1
            k-=1
        # print(ans)
        return ans

        
# @lc code=end

