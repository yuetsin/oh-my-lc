#!/usr/bin/env python

from functools import lru_cache


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        result = {}

        for allow in allowed:
            tp = (allow[0], allow[1])
            # for tp in [(allow[0], allow[1]), (allow[1], allow[0])]:
            if tp in result:
                result[tp].add(allow[2])
            else:
                result.update({tp: set([allow[2]])})

        # print(result)

        @lru_cache(maxsize=None)
        def buildOn(bottom: str) -> bool:
            # print('test', bottom)
            if len(bottom) == 1:
                return True

            possible = [()]

            for i in range(len(bottom) - 1):
                new_possible = []
                gotcha = (bottom[i], bottom[i + 1])
                if not gotcha in result:
                    return False

                for key in result[gotcha]:
                    for pos in possible:
                        new_possible.append(pos + (key,))

                possible = new_possible

            for item in possible:
                if buildOn(''.join(item)):
                    return True

            return False

        return buildOn(bottom)
