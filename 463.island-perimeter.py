#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (62.65%)
# Likes:    1477
# Dislikes: 97
# Total Accepted:    167.9K
# Total Submissions: 267.1K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes" (water inside that isn't connected to the
# water around the island). One cell is a square with side length 1. The grid
# is rectangular, width and height don't exceed 100. Determine the perimeter of
# the island.
# 
# 
# 
# Example:
# 
# 
# Input:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# Output: 16
# 
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_sz = len(grid)
        if row_sz == 0: return 0
        col_sz = len(grid[0])
        vertical = horizontal = 0
        for i in range(row_sz):
            prev = 0
            for j in range(col_sz):
                cell = grid[i][j]
                if prev != cell:
                    vertical += 1
                    prev = cell
            if prev != 0:
                vertical += 1
                
        for j in range(col_sz):
            prev = 0
            for i in range(row_sz):
                cell = grid[i][j]
                if prev != cell:
                    horizontal += 1
                    prev = cell
            if prev != 0:
                horizontal += 1

        return horizontal + vertical

# @lc code=end

