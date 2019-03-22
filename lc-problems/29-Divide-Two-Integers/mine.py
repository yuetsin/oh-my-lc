class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        rst = int(dividend / divisor)

        if rst < pow(-2, 31):
            return pow(2, 31) - 1
        elif rst > pow(2, 31) - 1:
            return pow(2, 31) - 1
        else:
            return rst
