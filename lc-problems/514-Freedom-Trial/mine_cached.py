#!/usr/bin/env python


from functools import lru_cache


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        ring_size = len(ring)
        key_size = len(key)

        @lru_cache(maxsize=1024)
        def dfs(ring_i: int, key_i: int) -> int:
            if key_i == key_size:
                return 0

            target_chr = key[key_i]

            possible_indexes = []
            for index in range(ring_size):
                if ring[index] == target_chr:
                    possible_indexes.append(index)

            min_actions = float('+inf')

            for posi in possible_indexes:
                # clockwise or anti-clockwise
                v = 1 + dfs(posi, key_i + 1) + min((ring_i - posi) %
                                                   ring_size, (posi - ring_i) % ring_size)

                min_actions = min(v, min_actions)

            return min_actions
        return dfs(0, 0)
