class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # print("Called isMatch: %s\n%s\n\n" % (s, p))

        anyCount = p.count('*')
        len_leak = len(s) - len(p) + anyCount + 1
        if anyCount != 0:
            
            if len_leak == 1:
                return self.isMatch(s, p.replace('*', ''))
            
            for i in range(8, 1, -1):
                p = p.replace('*' * i, '*')
        
        if anyCount == 0:
            if len(s) != len(p):
                return False
            for i in range(len(s)):
                if s[i] != p[i] and p[i] != '?':
                    return False
            return True
            
        first_id = p.find('*')
        if not self.isMatch(s[:first_id], p[:first_id]):
            return False
        
        last_id = p.rfind('*') - len(p) + 1
        if last_id != 0:
            if not self.isMatch(s[last_id:], p[last_id:]):
                return False
        
        for i in range(len_leak):
            if self.isMatch(s[first_id:], p.replace('*', '?' * i, 1)[first_id:]):
                return True
        return False

