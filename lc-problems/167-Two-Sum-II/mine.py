#!/usr/bin/env python


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        count = len(numbers)
        for i in range(count - 1):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, count):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                plus = numbers[i] + numbers[j]
                if plus == target:
                    return [i + 1, j + 1]
                elif plus > target:
                    break
        return []
