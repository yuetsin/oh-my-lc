#!/usr/bin/env python


class Solution:
    upper = set('QWERTYUIOPASDFGHJKLZXCVBNM')
    # lower = set('qwertyuiopasdfghjklzxcvbnm')

    def detectCapitalUse(self, word: str) -> bool:
        wordlen = len(word)
        if wordlen < 2:
            # 0 and 1 will always be fine
            return True

        upper_cnt = 0
        # lower_cnt = 0
        for char in word:
            if char in self.upper:
                upper_cnt += 1
            # else:
            #     lower_cnt += 1

        if upper_cnt == 0 or upper_cnt == wordlen:
            return True
        elif upper_cnt == 1 and word[0] in self.upper:
            return True
        else:
            return False
