#!/usr/bin/env python

# if (x,y in matrix) and (matrix[i][j]<matrix[x][y]):
# dp[i][j] = max(dp[i-1][j], dp[i+1][j], dp[i][j-1], dp[i][j+1])+1


class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        self.row, self.col = len(matrix), len(matrix[0])
        self.dp = [[0]*self.col for _ in range(self.row)]
        res = 0
        for i in range(self.row):
            for j in range(self.col):
                self.dp[i][j] = self.dfs(matrix, i, j)
                if self.dp[i][j] > res:
                    res = self.dp[i][j]
        return res

    def dfs(self, matrix, i, j):
        if self.dp[i][j] != 0:  # dp[i][j]!=0 indicates it has been visited
            return self.dp[i][j]
        max_path = 1
        if i-1 >= 0 and matrix[i][j] < matrix[i-1][j]:
            len_path = self.dfs(matrix, i-1, j)+1
            max_path = max(len_path, max_path)
        if i+1 < self.row and matrix[i][j] < matrix[i+1][j]:
            len_path = self.dfs(matrix, i+1, j)+1
            max_path = max(len_path, max_path)
        if j-1 >= 0 and matrix[i][j] < matrix[i][j-1]:
            len_path = self.dfs(matrix, i, j-1)+1
            max_path = max(len_path, max_path)
        if j+1 < self.col and matrix[i][j] < matrix[i][j+1]:
            len_path = self.dfs(matrix, i, j+1)+1
            max_path = max(len_path, max_path)
        self.dp[i][j] = max_path
        return self.dp[i][j]
