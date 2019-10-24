#!/usr/bin/env python

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n <= 0:
            return 1
        elif n == 1:
            return 10
        
        result = 10
        sumup = 9
        n -= 1
        counter = 9
        while n > 0:
            sumup *= counter
            result += sumup
            n -= 1
            counter -= 1
            
        return result