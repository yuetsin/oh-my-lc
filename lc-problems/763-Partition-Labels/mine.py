#!/usr/bin/env python


class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        unseparatable_tuples = []

        for alpha in 'qwertyuiopasdfghjklzxcvbnm':

            exists = []
            for i, ch in enumerate(S):
                if ch == alpha:
                    exists.append(i)

            if len(exists) < 2:
                continue

            unseparatable_tuples.append((exists[0], exists[-1]))

        unseparatable_tuples.sort()

        cutting_point = [0]

        # print(unseparatable_tuples)

        for i in range(1, len(S)):
            ok = True
            for begin, end in unseparatable_tuples:
                if begin < i and i <= end:
                    ok = False
                    break
            if ok:
                cutting_point.append(i)

        result = []

        # print(cutting_point)

        cutting_point.append(len(S))

        if len(cutting_point) <= 2:
            return [len(S)]

        for i in range(1, len(cutting_point)):
            result.append(cutting_point[i] - cutting_point[i - 1])

        return result
