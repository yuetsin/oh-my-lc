#!/usr/bin/env python


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.cached = {}

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if (row1, col1, row2, col2) in self.cached:
            return self.cached[(row1, col1, row2, col2)]
        result = 0
        for row in range(row1, row2 + 1):
            result += sum(self.matrix[row][col1:col2+1])
        self.cached.update({
            (row1, col1, row2, col2): result
        })
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
