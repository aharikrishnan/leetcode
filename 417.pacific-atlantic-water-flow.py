#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (39.23%)
# Likes:    978
# Dislikes: 188
# Total Accepted:    62.9K
# Total Submissions: 159.1K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
# 
# Note:
# 
# 
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# 
# 
# 
# Example:
# 
# 
# Given the following 5x5 matrix:
# 
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def dfs(self, matrix, i, j, color):
        if self.visited[i][j] & color:
            return
        self.visited[i][j] |= color
        if self.visited[i][j] == self.ATLANTIC | self.PACIFIC:
            self.res.append((i,j))
        directions = [(-1,0), (0,-1), (0,1), (1,0)]
        for ix, jy in directions:
            x,y = i+ix,j+jy
            if 0<= x < self.row_sz and 0<= y < self.col_sz and matrix[x][y] >= matrix[i][j]:
                self.dfs(matrix, x, y, color)

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        self.row_sz = len(matrix)
        if self.row_sz == 0: return
        self.col_sz = len(matrix[0])
        self.res = []

        self.PACIFIC = 1
        self.ATLANTIC = 2
        self.visited = [ [0]*self.col_sz for _ in range(self.row_sz)]

        for j in range(self.col_sz):
            self.dfs(matrix, 0,j,self.PACIFIC)
            self.dfs(matrix, self.row_sz-1,j,self.ATLANTIC)
        for i in range(self.row_sz):
            self.dfs(matrix, i,0,self.PACIFIC)
            self.dfs(matrix, i, self.col_sz-1,self.ATLANTIC)
        # print(self.visited)
        return self.res
        
# @lc code=end

# [
#     [9,9,9,9,9],
#     [9,0,0,0,9],
#     [9,0,9,0,9],
#     [9,0,0,0,9],
#     [9,9,9,9,9]
# ]
# [[0,0,0,0,0],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]