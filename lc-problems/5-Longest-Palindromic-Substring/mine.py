
class Solution:
    def isPalindromic(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        return False

    def longestPalindrome(self, s: str) -> str:

        str_len = len(s)

        if str_len == 0:
            return ""
        elif str_len == 1:
            return s
        substr_len = 2
        possible_rst = s[0]

        while substr_len <= str_len:
            flag = False

            for idx in range(str_len - substr_len + 1):
                if self.isPalindromic(s[idx: idx + substr_len]):
                    flag = True
                    possible_rst = s[idx: idx + substr_len]

                    break
            # if not flag:
            #     return possible_rst
            # else:
            substr_len += 1
        return possible_rst
