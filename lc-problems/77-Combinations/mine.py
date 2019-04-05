class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        rst = []
        if k == 1:
            for i in range(1, n + 1):
                rst.append([i])
            return rst
        elif n == k:
            return [list(range(1, k + 1))]
        else:
            for i in range(k, n + 1):
                lst = self.combine(i - 1, k - 1)
                for s in lst:
                    s.append(i)
                    rst.append(s)
            return rst
