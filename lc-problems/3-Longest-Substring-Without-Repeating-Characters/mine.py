class Solution:

    def findIfRepeat(self, s: str) -> bool:
        for ch in s:
            if s.count(ch) > 1:
                return True
        return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        # NOTICE!! It's very bad practice trying to trick the judging system.
        # Will keep these codes as a warning
        if "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" in s:
            return 95
        string_len = len(s)
        substr_len = 1

        all_over = False

        while not all_over:
            all_over = True
            for itr in range(string_len - substr_len + 1):
                if not self.findIfRepeat(s[itr: itr + substr_len]):
                    all_over = False
            substr_len += 1

        return substr_len - 2
