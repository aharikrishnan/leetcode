#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (42.00%)
# Likes:    1505
# Dislikes: 28
# Total Accepted:    123K
# Total Submissions: 291.6K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an integer matrix, find the length of the longest increasing path.
# 
# From each cell, you can either move to four directions: left, right, up or
# down. You may NOT move diagonally or move outside of the boundary (i.e.
# wrap-around is not allowed).
# 
# Example 1:
# 
# 
# Input: nums = 
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: nums = 
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row_sz = len(matrix)
        if row_sz == 0: return 0
        col_sz = len(matrix[0])
        dp = [([0] * col_sz) for _ in range(row_sz)]
        max_count = 0
        i=0
        while i < row_sz:
            j=0
            while j < col_sz:
                # print(i,j, dp)
                count = self.dfs(matrix,i,j, row_sz, col_sz, dp)
                max_count = max(max_count, count)
                j+=1
            i+=1
        return max_count
        
    def dfs(self, matrix, i,j, row_sz, col_sz, dp):
        if dp[i][j] != 0:
            return dp[i][j]
        neigh = [(0,-1), (-1,0), (0, 1), (1,0)]
        max_count = 0
        for ir, jc in neigh:
            r,c = i+ir, j+jc
            if (0<= r < row_sz) and (0<= c < col_sz) and matrix[r][c] > matrix[i][j] and (r,c) not in dp:
                neigh_count = self.dfs(matrix, r, c, row_sz, col_sz, dp)
                max_count  = max(max_count, neigh_count)
        dp[i][j] = max(dp[i][j], max_count+1)
        return dp[i][j]

        
# @lc code=end

