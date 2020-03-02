#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (41.33%)
# Likes:    1164
# Dislikes: 131
# Total Accepted:    108K
# Total Submissions: 260.3K
# Testcase Example:  '"abab"'
#
# Given a non-empty string check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together. You may assume
# the given string consists of lowercase English letters only and its length
# will not exceed 10000.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# 
# 
# Example 2:
# 
# 
# Input: "aba"
# Output: False
# 
# 
# Example 3:
# 
# 
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc"
# twice.)
# 
# 
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0: return False
        ss = s+s # If repeating it'll ateast have 4 of the repeating chars
        # a bababa b
        return ss[1:-1].find(s) != -1
# @lc code=end

