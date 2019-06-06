#!/usr/bin/env python


class Solution:
    def candy(self, ratings: List[int]) -> int:
        self.global_rst = [1] * len(ratings)

        def checkProblem() -> int:
            for i in range(1, len(ratings)):
                if ratings[i] > ratings[i - 1]:
                    if self.global_rst[i] <= self.global_rst[i - 1]:
                        return i
                elif ratings[i] < ratings[i - 1]:
                    if self.global_rst[i] >= self.global_rst[i - 1]:
                        return i - 1
            # All OK
            return -1

        last_badpoint = checkProblem()
        while last_badpoint != -1:
            self.global_rst[last_badpoint] += 1
            last_badpoint = checkProblem()

        # print(self.global_rst)
        return sum(self.global_rst)
