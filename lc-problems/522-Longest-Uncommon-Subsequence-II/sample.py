#!/usr/bin/env python

from collections import Counter


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # Checks if string `a` is a subsequence of `b`
        def subseq(a, b):
            if len(a) >= len(b):
                return False
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)

        count = Counter(strs)
        # Exlude all strings that occur in `strs` more than once
        exclude = [s for s, c in count.items() if c > 1]

        # Rest of the strings go to `check` array
        check = [s for s, c in count.items() if c == 1]
        # Sort by length from longest to shortest
        check.sort(key=lambda x: len(x), reverse=True)

        # If there are no items in exclude than longest strings is the answer
        if not exclude:
            return len(check[0])

            # Otherwise we need to check remaining strings one by one
        for s in check:
            # Check if string is subsequece of one of excluded
            for e in exclude:
                if subseq(s, e):
                    # If subsequence than mark current string as also exluded and go to next one
                    exclude.append(s)
                    break
                else:
                    # If not a subsequence than it's length is the answer
                    return len(s)

        return -1
