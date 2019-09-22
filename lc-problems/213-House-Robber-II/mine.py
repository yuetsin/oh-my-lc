#!/usr/bin/env python


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return max(nums[0], 0)
        elif length == 2:
            return max(nums)

        notailDP = {}
        withtailDP = {}

        def tryRob(since: int, notail: bool) -> int:
            if notail:
                if since > length - 2:
                    return 0
                if since in notailDP:
                    return notailDP[since]
            else:
                if since > length - 1:
                    return 0
                if since in withtailDP:
                    return withtailDP[since]
            maxVal = max(tryRob(since + 1, notail),
                         tryRob(since + 2, notail) + nums[since])
            if notail:
                notailDP.update({since: maxVal})
            else:
                withtailDP.update({since: maxVal})
            return maxVal

        return max(tryRob(0, True), tryRob(1, False))
