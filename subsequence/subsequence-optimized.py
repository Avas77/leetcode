# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution(object):
    def isSubsequence(self, s, t):
        s_len, t_len = len(s), len(t)
        if s_len > t_len:
            return False
        si = ti = 0
        while si < s_len and ti < t_len:
            if s[si] == t[ti]:
                si += 1
                ti += 1
            else:
                ti += 1
        return si == s_len
       


sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))
        