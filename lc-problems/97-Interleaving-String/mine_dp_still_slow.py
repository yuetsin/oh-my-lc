class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len1 + len2

        DP = [[[None for h in range(len3 + 1)]
               for i in range(len2 + 1)] for j in range(len1 + 1)]

        def canGo(p1: int, p2: int, p3: int) -> bool:
            if DP[p1][p2][p3] != None:
                return DP[p1][p2][p3]

            if p1 == len1:
                DP[p1][p2][p3] = (s2[p2:] == s3[p3:])
                return DP[p1][p2][p3]
            if p2 == len2:
                DP[p1][p2][p3] = (s1[p1:] == s3[p3:])
                return DP[p1][p2][p3]

            possible = False
            if s3[p3] == s1[p1]:
                if canGo(p1 + 1, p2, p3 + 1):
                    possible = True
            if s3[p3] == s2[p2]:
                if canGo(p1, p2 + 1, p3 + 1):
                    possible = True
            DP[p1][p2][p3] = possible
            return possible
        return canGo(0, 0, 0)
