#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (48.78%)
# Likes:    1297
# Dislikes: 85
# Total Accepted:    278.7K
# Total Submissions: 568.3K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def getPaths(node, ancestors=[]):
            if not node:
                return []
            elif (node.left is None and node.right is None):
                res.append("->".join(ancestors+[str(node.val)]))
            else:
                getPaths(node.left, ancestors+[str(node.val)])
                getPaths(node.right, ancestors+[str(node.val)])
        getPaths(root)
        return res


# @lc code=end

