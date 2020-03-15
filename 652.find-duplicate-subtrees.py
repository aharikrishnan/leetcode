#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (48.46%)
# Total Accepted:    53.9K
# Total Submissions: 110.1K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given a binary tree, return all duplicate subtrees. For each kind of
# duplicate subtrees, you only need to return the root node of any one of
# them.
# 
# Two trees are duplicate if they have the same structure with same node
# values.
# 
# Example 1: 
# 
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
# 
# 
# The following are two duplicate subtrees:
# 
# 
# ⁠     2
# ⁠    /
# ⁠   4
# 
# 
# and
# 
# 
# ⁠   4
# 
# Therefore, you need to return above trees' root in the form of a list.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.idGen = collections.defaultdict()
        self.idGen.default_factory = self.idGen.__len__
        self.counter = {}
        self.res = []
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if not root: return None
        nodeId = self.idGen[root.val, self.helper(root.left), self.helper(root.right)]
        self.counter[nodeId] = self.counter.get(nodeId, 0) + 1
        if self.counter[nodeId] == 2:
            self.res.append(root)
        return nodeId 
