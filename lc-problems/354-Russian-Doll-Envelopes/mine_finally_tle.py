#!/usr/bin/env python


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if envelopes == []:
            return 0

        Steps = [-1] * len(envelopes)
        def findMax(since: int) -> int:

            if Steps[since] != -1:
                return Steps[since]

            # print("called", since)
            result = 1

            for env in range(len(envelopes)):
                if env == since:
                    continue
                if envelopes[since][0] < envelopes[env][0] and envelopes[since][1] < envelopes[env][1]:
                    if Steps[env] == -1:
                        result = max(result, findMax(env) + 1)
                    else:
                        result = max(result, Steps[env] + 1)

            Steps[since] = result
            return result

        for i in range(1):
            print("find ", i, "is: ", findMax(i))

        # print(Steps)
        return max(Steps)
