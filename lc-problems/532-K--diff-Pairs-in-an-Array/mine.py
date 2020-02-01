import collections


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        if k != 0:
            sets = set(nums)
            counter = 0
            for num in sets:
                if num + k in sets:
                    counter += 1
            return counter
        else:
            c = dict(collections.Counter(nums))
            counter = 0
            for k, v in c.items():
                if v >= 2:
                    counter += 1
            return counter
