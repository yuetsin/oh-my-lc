#!/usr/bin/env python


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def pat(a, bw, cs):
            for n in cs:
                if n in bw:
                    a.append(bw.index(n))
                else:
                    bw.append(n)
                    a.append(bw.index(n))
            return a
        pn, ps, strl = [], [], str.split()
        pn = pat([], [], pattern)
        ps = pat([], [], strl)
        if pn == ps:
            return True
        else:
            return False
