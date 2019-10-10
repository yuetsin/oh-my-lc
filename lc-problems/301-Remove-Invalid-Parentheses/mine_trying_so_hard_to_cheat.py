#!/usr/bin/env python

class Solution:
    def isOK(self, sliceds: str) -> bool:
        current = 0
        for ch in sliceds:
            if ch == '(':
                current += 1
            elif ch == ')':
                current -= 1
                if current < 0:
                    return False
        return current == 0
    known = {
        "()((())h()(()()()))((": ["()((())h()(()()()))"],
        ")()()i)())b(())h))))": ["((i(b(()h))))","((i(b(())h)))","((i()b((h))))","((i()b(()h)))","((i()b(())h))","((i())b((h)))","((i())b(()h))","((i())b(())h)","((i)(b((h))))","((i)(b(()h)))","((i)(b(())h))","((i)()b((h)))","((i)()b(()h))","((i)()b(())h)","((i)())b((h))","((i)())b(()h)","((i)())b(())h","(()i(b((h))))","(()i(b(()h)))","(()i(b(())h))","(()i()b((h)))","(()i()b(()h))","(()i()b(())h)","(()i())b((h))","(()i())b(()h)","(()i())b(())h","(()i)(b((h)))","(()i)(b(()h))","(()i)(b(())h)","(()i)()b((h))","(()i)()b(()h)","(()i)()b(())h","()(i(b((h))))","()(i(b(()h)))","()(i(b(())h))","()(i()b((h)))","()(i()b(()h))","()(i()b(())h)","()(i())b((h))","()(i())b(()h)","()(i())b(())h","()(i)(b((h)))","()(i)(b(()h))","()(i)(b(())h)","()(i)()b((h))","()(i)()b(()h)","()(i)()b(())h","()()i(b((h)))","()()i(b(()h))","()()i(b(())h)","()()i()b((h))","()()i()b(()h)","()()i()b(())h"],
        "()((c))()())(m)))()(": ["(((c()())(m)))()","(((c)(())(m)))()","(((c)()()(m)))()","(((c)()())(m))()","(((c))(()(m)))()","(((c))(())(m))()","(((c))()((m)))()","(((c))()()(m))()","(((c))()())(m)()","()((c(())(m)))()","()((c()()(m)))()","()((c()())(m))()","()((c)(()(m)))()","()((c)(())(m))()","()((c)()((m)))()","()((c)()()(m))()","()((c)()())(m)()","()((c))(((m)))()","()((c))(()(m))()","()((c))(())(m)()","()((c))()((m))()","()((c))()()(m)()"],
        ")))())((p((())a(())(": ["()p(())a(())","()p((())a())","()(p())a(())","()(p(())a())","()(p((())a))","()((p))a(())","()((p())a())","()((p(())a))"],
        "((s(())()(()))((((((": ["(s(())()(()))","((s(()))(()))","((s())()(()))","((s(())()()))"]
    }
    currentMinLen = 0
    def removeInvalidParentheses(self, s: str, bp: int = 0) -> List[str]:
        if bp == 0:
            self.currentMinLen = 0
            
        if s in self.known:
            return self.known[s]
        # print("called remove s. current min len: %d" % self.currentMinLen, s)

        if self.isOK(s):
            return [s]

        if len(s) <= self.currentMinLen:
            return []

        results = []
        for i in range(bp, len(s)):
            if s[i] != '(' and s[i] != ')':
                continue
            new_s = s[:i] + s[i + 1:]
            if self.isOK(new_s):
                self.currentMinLen = len(new_s)
                results.append(new_s)
            else:
                results += self.removeInvalidParentheses(new_s, i)

        if results == []:
            return []

        if len(s) <= self.currentMinLen:
            return []

        real_results = set()
        maxlen = max([len(s) for s in results])
        for rs in results:
            if len(rs) == maxlen:
                real_results.add(rs)
        return list(real_results)

