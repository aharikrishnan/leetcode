#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#
# https://leetcode.com/problems/create-maximum-number/description/
#
# algorithms
# Hard (26.19%)
# Total Accepted:    36.1K
# Total Submissions: 136.6K
# Testcase Example:  '[3,4,6,5]\n[9,1,2,5,8,3]\n5'
#
# Given two arrays of length m and n with digits 0-9 representing two numbers.
# Create the maximum number of length k <= m + n from digits of the two. The
# relative order of the digits from the same array must be preserved. Return an
# array of the k digits.
# 
# Note: You should try to optimize your time and space complexity.
# 
# Example 1:
# 
# 
# Input:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# Output:
# [9, 8, 6, 5, 3]
# 
# Example 2:
# 
# 
# Input:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# Output:
# [6, 7, 6, 0, 4]
# 
# Example 3:
# 
# 
# Input:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# Output:
# [9, 8, 9]
# 
#
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        return max(self.merge(self.takeMax(nums1, i), self.takeMax(nums2, k-i))
                for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))
    
    def takeMax(self, xs, k):
        stack= []
        drop = len(xs) - k
        for x in xs:
            while drop and stack and stack[-1] < x:
                stack.pop()
                drop -= 1
            stack.append(x)
        return stack[:k]
  
    def merge(self, xs, ys):
        zs = []
        i,j=0,0
        while i < len(xs) and j < len(ys):
            if xs[i:] > ys[j:]:
                zs.append(xs[i])
                i+=1
            else:
                zs.append(ys[j])
                j+=1
        if i < len(xs): zs.extend(xs[i:])
        if j < len(ys): zs.extend(ys[j:])
        #print(xs,ys,zs)
        return zs 
