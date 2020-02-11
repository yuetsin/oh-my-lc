#!/usr/bin/env python

from functools import lru_cache


class Solution:

    alpha = 'qwertyuiopasdfghjklzxcvbnm'
    def minStickers(self, stickers: List[str], target: str) -> int:

        target = dict(collections.Counter(target))

        t_targ = []
        for i in self.alpha:
            if i in target:
                t_targ.append(target[i])
            else:
                t_targ.append(0)

        stickk = []

        for sticker in stickers:
            d = dict(collections.Counter(sticker))

            t_sti = []
            for i in self.alpha:
                if i in d:
                    t_sti.append(d[i])
                else:
                    t_sti.append(0)
            stickk.append(t_sti)

#         print("stick: ")
#         print(stickk)

#         print("======")

        @lru_cache(maxsize=None)
        def sticker(target: tuple) -> int:
            # print(target)
            count = float('+inf')

            for gotta in stickk:

                new_c = []

                for i in range(26):
                    if gotta[i] < target[i]:
                        new_c.append(target[i] - gotta[i])
                    else:
                        new_c.append(0)

                if sum(new_c) == 0:
                    return 1
                if tuple(new_c) != target:
                    count = min(count, 1 + sticker(tuple(new_c)))

            return count

        v = sticker(tuple(t_targ))

        if v == float('+inf'):
            return -1
        return v
