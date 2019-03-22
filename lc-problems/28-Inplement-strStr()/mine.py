class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haylen = len(haystack)
        needlen = len(needle)

        if needlen == 0:
            return 0

        if haylen < needlen:
            return -1
        if haylen == needlen:
            return 0 if haystack == needle else -1

        for i in range(haylen - needlen + 1):
            if haystack[i: i + needlen] == needle:
                return i

        return -1
