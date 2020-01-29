#!/usr/bin/env python


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lines = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        result = []
        for org_word in words:
            if org_word == '':
                result.append(org_word)
                continue

            word = org_word.lower()

            for line in range(len(lines)):
                if word[0] in lines[line]:
                    key = line

            ok = True
            for ch in word:
                if not ch in lines[key]:
                    ok = False
                    break

            if ok:
                result.append(org_word)

        return result
