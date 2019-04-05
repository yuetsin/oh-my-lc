# Space Complexity: O(m + n)


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            for k in range(len(matrix[i])):
                matrix[i][k] = 0

        for j in cols:
            for k in range(len(matrix)):
                matrix[k][j] = 0
