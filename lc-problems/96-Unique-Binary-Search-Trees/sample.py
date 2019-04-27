import math


class Solution(object):
    def numTrees(self, n):
        # Catalan Number  (2n)!/((n+1)!*n!)
        return math.factorial(2 * n)/(math.factorial(n)*math.factorial(n+1))
