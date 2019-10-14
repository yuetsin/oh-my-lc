#!/usr/bin/env python


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # You must make sure your result is the smallest in lexicographical order among all possible results.
        # 这句话简直是……不知道增大了多少难度。
        # 当然如果没有这句话……就没有任何难度了
        dictionary = {}
        for i in range(len(s)):
            if s[i] in dictionary:
                dictionary[s[i]].append(i)
            else:
                dictionary.update({
                    s[i]: [i]
                })

        new_s = []
        print(dictionary)
        counter = -1
        for ch in s:
            print("consider", ch)
            if not ch in dictionary:
                continue

            counter += 1
            if len(dictionary[ch]) < 2:
                # we can't remove it anyway
                print("add", ch)
                new_s.append(ch)
                dictionary.pop(ch)
                continue

            size = ord(ch) - ord('a')

            flag = False
            for i in range(size):
                if s.find(chr(i + 97), counter) != -1:
                    # remove me
                    dictionary[ch].pop()
                    flag = True

            if flag:
                continue

            print("add", ch)
            new_s.append(ch)
            # determined.
            dictionary.pop(ch)

        return ''.join(new_s)
