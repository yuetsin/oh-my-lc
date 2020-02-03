#!/usr/bin/env python


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sums = [0]
        cnt = 0
        for num in nums:
            cnt += num
            pre_sums.append(cnt)

        # print(pre_sums)

        num_cnt = len(nums)

        result = 0
        for i in range(1, num_cnt + 1):
            for j in range(i, num_cnt + 1):
                # print("i, j = %d, %d" % (i, j))
                if pre_sums[j] - pre_sums[i - 1] == k:
                    result += 1

        return result
