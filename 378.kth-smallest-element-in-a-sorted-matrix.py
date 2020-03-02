#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (52.01%)
# Likes:    1806
# Dislikes: 107
# Total Accepted:    155.2K
# Total Submissions: 296.9K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
# 
# 
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
# 
# 
# Example:
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# return 13.
# 
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n^2.
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row_sz = len(matrix)
        if row_sz == 0: return None
        col_sz = len(matrix[0])
        start, end = matrix[0][0], matrix[row_sz-1][col_sz-1]
        while start < end:
            mid = (start+end)//2
            count_lt = self.count_lt(matrix, row_sz, col_sz, mid)
            if count_lt < k:
                start = mid + 1 
            else:
                end = mid
        return end

    def count_lt(self, matrix, row_sz, col_sz, val):
        i,j = row_sz-1,0
        count = 0
        while i >= 0 and j < col_sz:
            if matrix[i][j] <= val:
                count += (i+1)
                j += 1
            else:
                i -= 1
        return count


        
# @lc code=end

