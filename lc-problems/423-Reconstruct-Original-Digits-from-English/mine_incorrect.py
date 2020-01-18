#!/usr/bin/env python


class Solution:
    def originalDigits(self, s: str) -> str:
        word_map = ['zero', 'one', 'two', 'three', 'four', 'five',
                    'six', 'seven', 'eight', 'nine']

        word_chr_map = [{'z': 1, 'e': 1, 'r': 1, 'o': 1},
                        {'o': 1, 'n': 1, 'e': 1},
                        {'t': 1, 'w': 1, 'o': 1},
                        {'t': 1, 'h': 1, 'r': 1, 'e': 2},
                        {'f': 1, 'o': 1, 'u': 1, 'r': 1},
                        {'f': 1, 'i': 1, 'v': 1, 'e': 1},
                        {'s': 1, 'i': 1, 'x': 1},
                        {'s': 1, 'e': 2, 'v': 1, 'n': 1},
                        {'e': 1, 'i': 1, 'g': 1, 'h': 1, 't': 1},
                        {'n': 2, 'i': 1, 'e': 1}]
        ntwhfuiivsg

        def build_map_dict(s: str) -> dict:
            result = {}
            for ch in s:
                if ch in result:
                    result[ch] += 1
                else:
                    result.update({ch: 1})
            return result

        r = build_map_dict(s)

        digits = []

        def has_remains(r: dict) -> bool:
            count = 0
            for c, v in r.items():
                count += v

            return count != 0

        while has_remains(r):
            found = False
            counter = -1
            for word in word_chr_map:
                # print("check", word)
                counter += 1
                ok = True
                for ch, count in word.items():
                    if not ch in r:
                        ok = False
                        break
                    if r[ch] < count:
                        ok = False
                        break
                if ok:
                    found = True
                    for ch, count in word.items():
                        r[ch] -= count
                    digits.append(str(counter))
                    break

            if not found:
                print("Not found as ", r)
                assert(False)

        # print(digits)
        digits.sort()
        return ''.join(digits)
