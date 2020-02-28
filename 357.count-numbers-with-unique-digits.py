#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#
# https://leetcode.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (47.83%)
# Likes:    328
# Dislikes: 758
# Total Accepted:    71.4K
# Total Submissions: 149.2K
# Testcase Example:  '2'
#
# Given a non-negative integer n, count all numbers with unique digits, x,
# where 0 ≤ x < 10^n.
# 
# 
# Example:
# 
# 
# Input: 2
# Output: 91 
# Explanation: The answer should be the total numbers in the range of 0 ≤ x <
# 100, 
# excluding 11,22,33,44,55,66,77,88,99
# 
# 
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return self.helper(min(10,n)) # By pigeon-hole principle
    
    def helper(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return 10
        else:
            c = 9
            n_digits = c
            for _ in range(n-1):
                n_digits *= c
                c -= 1
            return n_digits + self.helper(n-1)
        
# @lc code=end

