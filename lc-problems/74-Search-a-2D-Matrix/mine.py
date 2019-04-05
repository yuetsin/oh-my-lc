class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if matrix == None or matrix == []:
            return False
        new_line = matrix[0]
        if new_line == []:
            return False
        if new_line[0] > target:
            return False
        if new_line[-1] < target:
            return self.searchMatrix(matrix[1:], target)
        try:
            new_line.index(target)
            return True
        except ValueError:
            return False
