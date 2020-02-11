#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_sz, s_sz = len(p), len(s)
        p_idx, s_idx = 0, 0
        star_idx, s_match_idx = -1, -1

        while s_idx < s_sz:
            if p_idx < p_sz and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
                #print("Char matched ", s_idx, p_idx)
                s_idx += 1
                p_idx += 1
            elif p_idx < p_sz and p[p_idx] == '*':
                #print("* with 0 match", s_idx, p_idx)
                # try with 0 matches
                star_idx = p_idx
                s_match_idx = s_idx
                p_idx += 1
            elif star_idx == -1:
                return False
            else:
                #print("backtrack * with +1 match", s_idx, p_idx)
                # Backtrack match additional one char
                s_idx = s_match_idx + 1
                p_idx = star_idx + 1
                s_match_idx = s_idx

        #print("Out with ", s_idx, p_idx)
        return s_idx == s_sz and all(x == '*' for x in p[p_idx:])

# @lc code=end
