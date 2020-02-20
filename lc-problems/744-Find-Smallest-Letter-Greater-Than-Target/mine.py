#!/usr/bin/env python


class Solution:

    alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = alpha.find(target)

        for i in range(idx + 1, 56):
            if alpha[i] in letters:
                return i
