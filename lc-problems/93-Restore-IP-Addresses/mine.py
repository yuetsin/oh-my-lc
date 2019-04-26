class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []
        def parseIp(s: str, count: int) -> List[List[int]]:
            if len(s) > count * 3:
                # Impossible.
                return []
            if count == 0:
                # One empty solution
                return [[]]
            if count == 1:
                if len(s) != 1 and s[0] == '0':
                    # No solution
                    return []
                integer = int(s)
                if integer > 255:
                    # No solution
                    return []
                return [[s]]
            # Count > 1:
            possible = []
            
            possible += [[s[0]] + l for l in parseIp(s[1:], count - 1)]
            
            if s[0] != '0':
                try:
                    possible += [[s[:2]] + l for l in parseIp(s[2:], count - 1)]
                except:
                    pass
                try:
                    integer = int(s[:3])
                    if integer < 256:
                        possible += [[s[:3]] + l for l in parseIp(s[3:], count - 1)]
                except:
                    pass
            return possible
        return ['.'.join(i) for i in parseIp(s, 4)]