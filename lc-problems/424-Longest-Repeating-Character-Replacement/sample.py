#!/usr/bin/env python


def characterReplacement(self, s: str, k: int) -> int:
    if not s:
        return 0
    # 1. keep track of counts per char
    d = collections.defaultdict(int)
    d[s[0]] += 1
    # 2. keep track of count of char with max occurence
    max_char_count = 1
    # 3. keep track of starting point of sliding window
    start = 0
    # 4. store the global max sliding window len
    max_window_len = 1
    for i in range(1, len(s)):
        d[s[i]] += 1
        # 5. keep count of char with max occurence current
        max_char_count = max(max_char_count, d[s[i]])
        # 6. at each i we can calculate how many replacements we have used = current_window_size - max_char_count
        # if this number if greater than k, we need to move our sliding starting window up one position and substract the that count
        while i-start+1-max_char_count > k:
            d[s[start]] -= 1
            start += 1
            # 7. update global max sliding window length
        max_window_len = max(max_window_len, i-start+1)
    return max_window_len
