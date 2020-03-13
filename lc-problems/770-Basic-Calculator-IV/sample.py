#!/usr/bin/env python
#
# written by @yuanzhi247012

import re


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        exps = (re.sub(r'([\+\*\(\)])', r' \1 ',
                       expression.replace('-', '+(-1)*'))+' +').split()
        v1, v2, stack = [], [], []
        symbolVals = {a: str(b) for a, b in zip(evalvars, evalints)}
        for v in exps:
            v = symbolVals.get(v, v)
            if v == '(':
                stack.append([v1, v2])
                v1, v2 = [], []
            elif v == ')':
                v3 = v1+v2
                v1, v2 = stack.pop()
                v2 = [x2+'*'+x3 for x2 in v2 for x3 in v3] if v2 else v3
            elif v == '*':
                pass
            elif v == '+':
                v1, v2 = v1+v2, []
            else:
                v2 = [x+'*'+v for x in v2] if v2 else [v]

        def orderMultiply(x):
            factor, res = 1, []
            for v in x.split('*'):
                try:
                    factor *= int(v)
                except:
                    res.append(v)
            return [factor, '*'.join(sorted(res))]
        d = collections.defaultdict(int)
        for v in v1:
            factor, exp = orderMultiply(v)
            d[exp] += factor

        def keyComparer(x): return [
            0, []] if not x else [-len(x.split('*')), x.split('*')]
        return [str(d[key])+('*'+key if key else '') for key in sorted(d, key=keyComparer) if d[key]]
