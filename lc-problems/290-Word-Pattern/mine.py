#!/usr/bin/env python


class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:

        def convertDictionary(chars: List[str]) -> List[int]:
            visited = []

            result = []
            for char in chars:
                try:
                    rs = visited.index(char)
                    result.append(rs)
                except:
                    visited.append(char)
                    result.append(len(visited) - 1)
            return result

        return convertDictionary(list(pattern)) == convertDictionary(string.split(' '))
