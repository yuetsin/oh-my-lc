#!/usr/bin/env python

import string

ch_to_bit = {ch: 1 << i for i, ch in enumerate(string.ascii_lowercase)}


def Compact(words):
    # Word as int ==> wint
    wint_to_len = {}
    for w in words:
        w_n = len(w)
        wint = sum([ch_to_bit[ch] for ch in set(w)])
        # among duplicates, only the largest length is used.
        wint_to_len[wint] = max(w_n, wint_to_len.get(wint, 0))

    return wint_to_len


def CompareUntilUseless(wint_to_len):
    max_product = 0

    # Sorting the list allows skipping entries too small to make a difference
    wint_len_pairs = [(wint, w_len) for wint, w_len in wint_to_len.items()]
    wint_len_pairs.sort(reverse=True, key=lambda x: x[1])  # x[1] is length

    num_pairs = len(wint_len_pairs)
    for i in range(0, num_pairs - 1):
        wint, w_len = wint_len_pairs[i]
        # All remaining entries are size w_len or smaller
        if w_len * w_len <= max_product:
            break
        for cmpint, cmp_len in wint_len_pairs[i+1:]:
            if wint & cmpint == 0:
                max_product = max(max_product, w_len * cmp_len)

    return max_product


class Solution:
    def maxProduct(self, words):
        return CompareUntilUseless(Compact(words))
