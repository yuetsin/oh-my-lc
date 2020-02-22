from functools import lru_cache


class Solution:

    successor = {'0': '1', '1': '2', '2': '3', '3': '4',
                 '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '0'}

    predecessor = {'1': '0', '2': '1', '3': '2', '4': '3',
                   '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '0': '9'}

    def openLock(self, deadends: List[str], target: str) -> int:

        deadends_set = set(deadends)

        visited_set = set()

        # @lru_cache(maxsize=10000)
        def tryy(since: str) -> int:

            # print('called tryy with', since)
            if since == target:
                return 0

            if since in deadends_set:
                return float('+inf')

            if since in visited_set:
                return float('+inf')

            visited_set.add(since)

            digits = list(since)

            result = float('+inf')
            for i in range(4):
                orig = digits[i]

                digits[i] = self.successor[orig]
                result = min(result, tryy(''.join(digits)))

                digits[i] = self.predecessor[orig]
                result = min(result, tryy(''.join(digits)))

                digits[i] = orig

            visited_set.remove(since)
            return result + 1

        ret = tryy('0000')

        return ret if ret != float('+inf') else -1
