#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (58.53%)
# Likes:    1059
# Dislikes: 90
# Total Accepted:    128.9K
# Total Submissions: 219K
# Testcase Example:  '"tree"'
#
# Given a string, sort it in decreasing order based on the frequency of
# characters.
# 
# Example 1:
# 
# Input:
# "tree"
# 
# Output:
# "eert"
# 
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
# 
# 
# 
# Example 2:
# 
# Input:
# "cccaaa"
# 
# Output:
# "cccaaa"
# 
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# 
# 
# 
# Example 3:
# 
# Input:
# "Aabb"
# 
# Output:
# "bbAa"
# 
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
# 
# 
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        sz = len(s)
        if sz == 0: return ''

        freq = {}
        for c in s:
            freq[c] = freq.get(c,0) + 1
        reverse_freq = {}
        for c in freq:
            v = freq[c]
            if v in reverse_freq:
                reverse_freq[v].append(c)
            else:
                reverse_freq[v] = [c]
        # print(reverse_freq)
        res = []
        for i in range(sz,0, -1):
            if i in reverse_freq:
                for c in reverse_freq[i]:
                    res.append(c*i)
        return "".join(res)
        
# @lc code=end

