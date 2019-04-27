class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len1 + len2

        def canGo(p1: int, p2: int, p3: int) -> bool:
            if p1 == len1:
                return s2[p2:] == s3[p3:]
            if p2 == len2:
                return s1[p1:] == s3[p3:]

            possible = False
            if s3[p3] == s1[p1]:
                if canGo(p1 + 1, p2, p3 + 1):
                    possible = True
            if s3[p3] == s2[p2]:
                if canGo(p1, p2 + 1, p3 + 1):
                    possible = True
            return possible
        return canGo(0, 0, 0)
