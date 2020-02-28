#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (40.65%)
# Likes:    2645
# Dislikes: 274
# Total Accepted:    414.8K
# Total Submissions: 1M
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# 
# Example:
# 
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# 
# 
# 
# 
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        

    def push(self, x: int) -> None:
        min_so_far = self.getMin()
        if min_so_far is None or min_so_far > x:
            min_so_far = x
        self.arr.append((x, min_so_far))

    def pop(self) -> None:
        if len(self.arr):
            x, _ = self.arr.pop()
            return x

    def top(self) -> int:
        x, _ = self._top()
        return x

    def getMin(self) -> int:
        _, min_so_far = self._top()
        return min_so_far

    def _top(self):
        top = self.arr[-1] if len(self.arr) else (None, None)
        return top


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

