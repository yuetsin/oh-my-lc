class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # print("isMatch(%s, %s) called" % (s, p))

        if (p == '.' and len(s) == 1) or s == p:
            # print(p == '.' or s == p)
            return True

        if len(p) < 2:
            return p == s

        if len(s) == 0:
            if p[1] == '*' and len(p) >= 2:
                return self.isMatch(s, p[2:])
            return False

        if p[1] == '*':
            max_expand_limit = len(s) + 2 * p.count('*') - len(p)
            # print(max_expand_limit)
            repeat_chr = p[0]

            for repeat_count in range(max_expand_limit + 1):

                newp = repeat_count * repeat_chr + p[2:]

                if self.isMatch(s, newp):
                    # print(True)
                    return True
            # print(False)
            return False
        else:
            if s[0] != p[0]:
                if p[0] != '.':
                    return False
            return self.isMatch(s[1:], p[1:])
