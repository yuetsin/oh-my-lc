#!/usr/bin/env python


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if envelopes == []:
            return 0

        def canFit(env1: List[int], env2: List[int]) -> bool:
            return env1[0] < env2[0] and env1[1] < env2[1]

        Paths = [[] for _ in range(len(envelopes))]

        for envInIndex in range(len(envelopes)):
            for envOutIndex in range(len(envelopes)):
                if envInIndex == envOutIndex:
                    continue
                if canFit(envelopes[envInIndex], envelopes[envOutIndex]):
                    Paths[envInIndex].append(envOutIndex)

        # print(Paths)

        Steps = [-1] * len(envelopes)

        def findMax(since: int) -> int:
            if Steps[since] != -1:
                return Steps[since]
            result = 1
            if Paths[since]:
                for nextStep in Paths[since]:
                    result = max(result, findMax(nextStep) + 1)
            else:
                Steps[since] = 1
                return 1
            Steps[since] = result
            return result

        for i in range(len(envelopes)):
            findMax(i)

        return max(Steps)
