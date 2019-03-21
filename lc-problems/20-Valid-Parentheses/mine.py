class Solution:

    charmap = {
        ')': -1,
        ']': -2,
        '}': -3,
        '(': 1,
        '[': 2,
        '{': 3
    }

    def match(self, s1: str, s2: str) -> bool:
        try:
            return self.charmap[s1] + self.charmap[s2] == 0
        except KeyError:
            return False

    def isValid(self, s: str) -> bool:
        strlen = len(s)
        if strlen == 0:
            return True
        # lptr = 0
        lchar = s[0]
        rptr = 0

        rec_count = 0
        while rptr + 1 < strlen:
            rptr += 1
            if lchar == s[rptr]:
                rec_count += 1
                continue
            if self.charmap[lchar] + self.charmap[s[rptr]] == 0:
                if rec_count == 0:
                    if rptr + 1 == strlen:
                        return self.isValid(s[1: rptr])
                    return self.isValid(s[1: rptr]) and self.isValid(s[rptr + 1:])
                else:
                    rec_count -= 1
        return False
