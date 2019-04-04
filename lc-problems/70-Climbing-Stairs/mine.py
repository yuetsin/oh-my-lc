class Solution:
    DP = []

    def climbStairs(self, n: int) -> int:
        if self.DP == []:
            self.DP = [-1] * (n + 1)
            self.DP[0] = 0
            self.DP[1] = 1
            if n > 1:
                self.DP[2] = 2
        if self.DP[n] != -1:
            return self.DP[n]
        else:
            self.DP[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return self.DP[n]
