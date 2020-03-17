#
# @lc app=leetcode id=330 lang=python3
#
# [330] Patching Array
#
# https://leetcode.com/problems/patching-array/description/
#
# algorithms
# Hard (34.02%)
# Total Accepted:    34.7K
# Total Submissions: 101.9K
# Testcase Example:  '[1,3]\n6'
#
# Given a sorted positive integer array nums and an integer n, add/patch
# elements to the array such that any number in range [1, n] inclusive can be
# formed by the sum of some elements in the array. Return the minimum number of
# patches required.
# 
# Example 1:
# 
# 
# Input: nums = [1,3], n = 6
# Output: 1 
# Explanation:
# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3,
# 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3],
# [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.
# 
# Example 2:
# 
# 
# Input: nums = [1,5,10], n = 20
# Output: 2
# Explanation: The two patches can be [2, 4].
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,2], n = 5
# Output: 0
# 
#
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # from a given range [1,x] we can form upto 2x
        miss = 1
        i = 0
        res = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i+=1
            else:
                miss += miss
                res += 1
        return res 
    
    def minPatchesNaive(self, nums: List[int], n: int) -> int:
        comb = set()
        for num in nums:
            comb.update( set(c+num for c in comb) | {num} )
        #print(comb)
        res = []
        for num in range(1,n+1):
            if num not in comb:
                res.append(num)
                comb.update( set(c+num for c in comb) | {num} )
                #print(comb)
            if len(comb) == n: break
        #print(res)
        return len(res)
                
                
            
         
