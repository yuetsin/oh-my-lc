class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sptr = 0
        pptr = 0
        starptr = -1
        strptr = 0
        slen = len(s)
        plen = len(p)
        s += '.'
        p += '.'
        
        while sptr < slen:
            if p[pptr] == '?' or s[sptr] == p[pptr]:
                sptr += 1
                pptr += 1
                continue
                
            if p[pptr] == '*':
                starptr = pptr
                pptr += 1
                strptr = sptr
                continue
            
            if starptr != -1:
                pptr = starptr + 1
                strptr += 1
                sptr = strptr
                continue
            
            return False
        
        while p[pptr] == '*':
            pptr += 1
        
        return pptr >= plen