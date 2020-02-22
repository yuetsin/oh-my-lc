#!/usr/bin/env python


class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        def tup(s):
            return tuple(map(int, s))

        initial = tup("0000")
        target = tup(target)
        deadends = set(map(tup, deadends))
        front, newfront = [initial], []
        seen = {initial}
        steps = 0

        while front:
            while front:
                s = front.pop()
                if s in deadends:
                    continue
                elif s == target:
                    return steps
                for i in range(4):
                    for d in (-1, 1):
                        old = s[i]
                        si = (10+old+d) % 10
                        ss = tuple(s[:i]+(si,)+s[i+1:])
                        if ss not in seen:
                            newfront.append(ss)
                            seen.add(ss)
            newfront, front = front, newfront
            steps += 1
        return -1
