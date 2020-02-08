#!/usr/bin/env python


class Solution:
    def replaceWords(self, dicts: List[str], sentence: str) -> str:
        sets = set(dicts)
        comp = sentence.split(' ')

        results = []
        for token in comp:
            found = False
            for i in range(1, len(token)):
                if token[:i] in sets:
                    results.append(token[:i])
                    found = True
                    break

            if not found:
                results.append(token)

        return ' '.join(results)
