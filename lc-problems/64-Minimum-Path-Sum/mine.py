class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        DP = [[-1 for col in range(n)] for row in range(m)]
        DP[0][0] = grid[0][0]

        def getMinPath(row: int, col: int) -> int:
            if row < 0 or col < 0:
                return 10000
            if DP[row][col] != -1:
                return DP[row][col]

            up = getMinPath(row - 1, col)
            left = getMinPath(row, col - 1)

            this = min(up, left) + grid[row][col]
            DP[row][col] = this
            return this

        # print("DP = %s" % (str(DP)))
        return getMinPath(m - 1, n - 1)
