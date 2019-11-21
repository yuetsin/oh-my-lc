#!/usr/bin/env python


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or len(s) < k:
            return 0
        if k < 2:
            return len(s)

        my_dict = {}
        for c in s:
            my_dict[c] = my_dict.get(c, 0) + 1

        left = 0
        partition = []
        for right in range(len(s)):
            if my_dict[s[right]] < k:
                partition.append(s[left:right])
                left = right + 1
        partition.append(s[left:])  # don't forget the last segment

        if len(partition) == 1:
            return len(s)

        res = 0
        for subs in partition:
            res = max(res, self.longestSubstring(subs, k))

        return res
