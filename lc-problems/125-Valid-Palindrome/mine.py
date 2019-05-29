#!/usr/bin/env python3


class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == "":
            return True

        string = ""
        for i in s.lower():
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                string += i

        return string == string[::-1]
