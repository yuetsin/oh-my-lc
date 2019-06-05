class Solution:

    DP = {}

    def minCut(self, s):
        res = []
        return self.dfs(s)

    def dfs(self, s) -> int:
        if not s in self.DP:
            if self.isPal(s):
                return 0
            if not s:
                return 0
            min_sp = 1048576
            for i in range(1, len(s) - 1):
                sp = self.dfs(s[:i]) + self.dfs(s[i:]) + 1
                if sp < min_sp:
                    min_sp = sp
                    if sp == 1:
                        break
            self.DP.update({s: min_sp})
        return self.DP[s]

    def isPal(self, s):
        return s == s[::-1]
