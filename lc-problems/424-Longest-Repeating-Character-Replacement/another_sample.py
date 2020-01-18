#!/usr/bin/env python


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hmap = collections.defaultdict(int)
        start = 0
        end = 0
        maximum = 0
        cur_high_count = 0

        while end < len(s):
            hmap[s[end]] += 1
            cur_high_count = max(cur_high_count, hmap[s[end]])
            while end - start + 1 - cur_high_count > k:
                hmap[s[start]] -= 1
                start += 1
            maximum = max(maximum, end-start+1)
            end += 1

        return maximum
