#!/usr/bin/env python


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        num_cnt = len(nums)
        if num_cnt < 2:
            return 0

        sums = [0]
        current_sum = 0

        for num in nums:
            if num == 0:
                current_sum += -1
            else:
                current_sum += 1
            sums.append(current_sum)

        result = 0
        # print(sums)
        for i in range(1, num_cnt):
            for j in range(i + 1, num_cnt + 1):
                if j - i + 1 <= result:
                    continue
                # print("Detect between [%d:%d]" % (i, j))
                if sums[j] - sums[i - 1] == 0:
                    result = j - i + 1

        return result
