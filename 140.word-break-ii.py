#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (29.50%)
# Likes:    1453
# Dislikes: 320
# Total Accepted:    198.3K
# Total Submissions: 670.6K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# 
#

# @lc code=start
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
            0------i------n
            0--(j)---i
            dp[i] = True if dp[j] + dict.contains(j..i) | for j in 0..i-1 |  for i in 0..n
        
            catsanddog
            
            N-ary tree:
            {
                10: [7]  - " dogs"
                7: [3,4] - "sand" "and"
                3: [0]  - "cat"
                4: [0]  - "cats"
            }

             10
             |
             7
            / \
           3   4
           |   |
           0   0
        """
        sz = len(s)
        dp = [False] * (sz+1)
        dp[0] = True
        T = {} # Tree
        for i in range(sz):
            for word in wordDict:
                wsz = len(word)
                if wsz <= i+1 and dp[i+1-wsz] and s[:i+1].endswith(word):
                    dp[i+1] = True
                    if i-wsz in T:
                        T[i-wsz].append(i)
                    else:
                        T[i-wsz] = [i]
        #print(T)
        #print(dp)
        ans = []
        if not dp[-1]: 
            return ans
        def inorder(node, prefix=""):
            for child in T[node]:
                if child == sz-1:
                    ans.append(prefix+s[node+1:child+1])
                elif child in T:
                        inorder(child, prefix+s[node+1:child+1]+" ")

        inorder(-1)
        #print(ans)
        return ans



#Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
#Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"])
#Solution().wordBreak("abcd", ["a","abc","b","cd"])
        
# @lc code=end

