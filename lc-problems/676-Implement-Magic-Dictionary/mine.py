#!/usr/bin/env python


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sets = set()

    def buildDict(self, dic: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.sets = set()
        for word in dic:
            self.sets.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """

        ok = False
        for dicword in self.sets:
            if len(dicword) == len(word):
                ok = True
                break

        if not ok:
            return False

        for i in range(len(word)):
            for ch in 'qwertyuiopasdfghjklzxcvbnm':
                if ch == word[i]:
                    continue
                if word[:i] + ch + word[i + 1:] in self.sets:
                    return True

        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
