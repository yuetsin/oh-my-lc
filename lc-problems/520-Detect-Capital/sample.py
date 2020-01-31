#!/usr/bin/env python


class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        # if it is a capital word, or of all upper-case letters already
        flag_capital = word.istitle() or word.isupper()

        # if it is of all lower-case letters already
        flag_all_lower_case = word.islower()

        if flag_capital or flag_all_lower_case:
            # Accept:
            return True

        else:
            # Reject:
            # this word breaks the rule
            return False
