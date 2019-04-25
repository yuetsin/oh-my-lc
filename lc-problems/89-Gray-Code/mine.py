#!/usr/bin/env python


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        # successive: 连续的
        bits = [False] * n

        def getExps(l: int) -> List[List[bool]]:
            if l == 1:
                return [[False], [True]]
            else:
                rst = getExps(l - 1)
                rst_i = copy.deepcopy(rst)
                rst_i.reverse()
                return [[False] + i for i in rst] + [[True] + j for j in rst_i]
        rtn = getExps(n)
        rst = []
        for i in rtn:
            length = len(i)
            number = 0
            for j in range(length):
                if i[length - 1 - j]:
                    number += pow(2, j)
            rst.append(number)
        return rst
