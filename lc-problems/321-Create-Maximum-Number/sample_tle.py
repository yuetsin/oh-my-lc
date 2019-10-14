#!/usr/bin/env python


class Solution(object):
    def maxNumber(self, nums1: List[int], nums2: List[int], length: int) -> List[int]:
        if len(nums1) + len(nums2) < length:
            return []

        dp = [[[0 for _ in range(length + 1)] for _ in range(len(nums2) + 1)]
              for _ in range(len(nums1) + 1)]
        for k in range(1, length + 1):
            for j in range(k, len(nums2) + 1):
                dp[0][j][k] = max(dp[0][j - 1][k], 10 * dp[0]
                                  [j - 1][k - 1] + nums2[j - 1])
            for i in range(k, len(nums1) + 1):
                dp[i][0][k] = max(dp[i - 1][0][k], 10 *
                                  dp[i - 1][0][k - 1] + nums1[i - 1])

            for i in range(1, len(nums1) + 1):
                for j in range(1, len(nums2) + 1):
                    if i + j < k:
                        continue
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1]
                                      [j][k], dp[i][j - 1][k])
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1]
                                      [j][k - 1] * 10 + nums1[i - 1])
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1]
                                      [k - 1] * 10 + nums2[j - 1])

        return map(int, list(str(dp[-1][-1][-1])))
