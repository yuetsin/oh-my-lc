#!/usr/bin/env python


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = {}
        used = {}
        stack = []
        for i in range(len(s)):
            if s[i] not in counts:
                counts[s[i]] = 1
            else:
                counts[s[i]] += 1
            used[s[i]] = False
        for i in range(len(s)):
            if used[s[i]]:
                counts[s[i]] -= 1
                continue
            while stack and stack[-1] > s[i] and counts[stack[-1]] > 1:
                counts[stack[-1]] -= 1
                used[stack[-1]] = False
                stack.pop()
            stack.append(s[i])
            used[s[i]] = True
        res = "".join(stack)
        return res
