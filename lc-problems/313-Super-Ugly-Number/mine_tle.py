#!/usr/bin/env python

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # 好嘛，动态给 primes，不能打表了
        def isUgly(num: int) -> bool:
            # primes count: k
            # time complexity: O(k * i)
            for p in primes:
                if p > num:
                    break
                while num % p == 0 < num:
                    num /= p
            return num == 1

        
        counter = 0
        for i in range(1, 2147483647):
            # isUgly will be called 2 ** 31 - 1 times at most.
            # actually it is decided by n...
            # k * (n ) * (n )
            if isUgly(i):
                counter += 1
                if counter == n:
                    return i
