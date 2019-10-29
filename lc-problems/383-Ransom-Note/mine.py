#!/usr/bin/env python


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if ransomNote.count(ch) > magazine.count(ch):
                return False
        return True
