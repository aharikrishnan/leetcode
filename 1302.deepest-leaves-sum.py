#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#
# https://leetcode.com/problems/deepest-leaves-sum/description/
#
# algorithms
# Medium (83.91%)
# Likes:    197
# Dislikes: 19
# Total Accepted:    18.1K
# Total Submissions: 21.7K
# Testcase Example:  '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
#
# Given a binary tree, return the sum of values of its deepest leaves.
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.deep_sum = 0
        self.max_level_so_far = 0
        self.helper(root)
        return self.deep_sum
        
    def helper(self, node, l=0):
        if node:
            self.helper(node.left, l+1)
            self.helper(node.right, l+1)
            if self.max_level_so_far < l:
                self.deep_sum = 0
                # print('Found deepest node ', l, node.val)
                self.max_level_so_far = l
            if self.max_level_so_far == l:
                # print('Adding to sum ', l, node.val, self.deep_sum)
                self.deep_sum+=node.val
# @lc code=end

