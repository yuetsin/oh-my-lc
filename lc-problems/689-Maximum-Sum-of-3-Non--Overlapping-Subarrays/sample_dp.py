#!/usr/bin/env python


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        if not n or not k or 3*k > n:
            return []

            # preprocess, get ksum start at index i
        sumK = [0]*(n-k+1)
        sumK[0] = sum(nums[:k])
        for i in range(1, n-k+1):
            sumK[i] = sumK[i-1] + nums[i+k-1] - nums[i-1]
        # print(sumK)

            # 1 subarray: track and record maxvalue in the range [0, i]
        maxSum = (-float('inf'), -1)
        dp0 = [(0, 0)]*(n-3*k+1)

        for i in range(len(dp0)):
            if sumK[i] > maxSum[0]:
                maxSum = (sumK[i], i)
            dp0[i] = maxSum

        # print(dp0)
            # 2 subarray: track and record maxvalue in the range [0, i]
            # for index i, the candidate could either be maxvalue in dp0 + current value or maxSum
        maxSum = (-float('inf'), -1, -1)
        dp1 = [(-float('inf'), -1, -1)]*(n-2*k+1)
        for i in range(k, n-2*k+1):
            tmp = sumK[i]+dp0[i-k][0]
            if tmp > maxSum[0]:
                maxSum = (tmp, dp0[i-k][1], i)
            dp1[i] = maxSum
        # print(dp1)
            # 3 subarray: track and record maxvalue in the range [0, i]
            # for index i, the candidate could either be maxvalue in dp1 + current value or maxSum
        maxSum = (-float('inf'), -1, -1, -1)
        dp2 = [(-float('inf'), -1, -1, -1)]*(n-k+1)
        for i in range(2*k, n-k+1):
            tmp = sumK[i]+dp1[i-k][0]
            if tmp > maxSum[0]:
                maxSum = (tmp, dp1[i-k][1], dp1[i-k][2], i)
            dp2[i] = maxSum

        return list(dp2[-1])[1:]
