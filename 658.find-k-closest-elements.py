#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (39.54%)
# Total Accepted:    81.7K
# Total Submissions: 206K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# 
# Given a sorted array, two integers k and x, find the k closest elements to x
# in the array.  The result should also be sorted in ascending order.
# If there is a tie,  the smaller elements are always preferred.
# 
# 
# Example 1:
# 
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# 
# 
# 
# 
# Example 2:
# 
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# 
# 
# 
# Note:
# 
# The value k is positive and will always be smaller than the length of the
# sorted array.
# ⁠Length of the given array is positive and will not exceed 10^4
# ⁠Absolute value of elements in the array and x will not exceed 10^4
# 
# 
# 
# 
# 
# 
# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list
# of integers). Please reload the code definition to get the latest changes.
# 
#
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sz = len(arr)
        pos = self.insertPosition(arr, x)
        left, right = float('inf'), float('inf')
        if pos - 1 >= 0:
            left = abs(x-arr[pos-1])
        if pos < sz:
            right = abs(x-arr[pos])
        #print(pos, left, right) 
        center = pos if right < left else pos - 1
        i = j = center
        k-=1
        while k > 0 and j+1 < sz and i-1 >= 0:
            if abs(x-arr[j+1]) < abs(x-arr[i-1]):
                j+=1
            else:
                i-=1
            k-=1
        while k > 0 and j+1 < sz:
            j+=1
            k-=1
        while k > 0 and i-1 >= 0:
            i-=1
            k-=1
        #print(center,i,j)
        res = arr[i:j+1] 
        return res
    
    def insertPosition(self, xs, x):
        lo,hi = 0, len(xs)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if xs[mid] <= x:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo  
