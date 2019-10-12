#!/usr/bin/env python


def nthSuperUglyNumber(self, n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    if n == 1:
        return 1
    nums = [1]
    m = len(primes)
    dp = [0 for i in range(m)]
    while n > 1:
        temp = []
        for i in range(m):
            temp.append(nums[dp[i]]*primes[i])
        mv = min(temp)
        for i in range(m):
            if nums[dp[i]]*primes[i] == mv:
                dp[i] += 1
        nums.append(mv)
        n -= 1
    return mv
