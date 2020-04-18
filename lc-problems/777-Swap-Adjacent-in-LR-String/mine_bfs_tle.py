#!/usr/bin/env python


class Solution:

    def canTransform(self, start: str, end: str) -> bool:

        def get_all_replaces(word: str, key: str, rep: str) -> List[str]:
            keylen = len(key)
            wordlen = len(word)

            result = []
            for i in range(wordlen - keylen + 1):
                if word[i: i + keylen] == key:
                    result.append(word[:i] + rep + word[i + keylen:])

            return result

        words = set()

        words.add(start)

        while True:
            if end in words:
                return True

            new_elems = []

            for word in words:
                if 'XL' in word:
                    new_elems += get_all_replaces(word, 'XL', 'LX')
                if 'LX' in word:
                    new_elems += get_all_replaces(word, 'RX', 'XR')

            flag = False
            for elem in new_elems:
                if not elem in words:
                    words.add(elem)
                    flag = True

            if not flag:
                return False
