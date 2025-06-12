class Solution:
    def rec(self, i, j, s1, s2, dp):
        if i < 0 or j < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        if s1[i] == s2[j]:
            dp[i][j] = 1 + self.rec(i - 1, j - 1, s1, s2, dp)
        else:
            dp[i][j] = max(self.rec(i - 1, j, s1, s2, dp), self.rec(i, j - 1, s1, s2, dp))
        
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.rec(m - 1, n - 1, text1, text2, dp)