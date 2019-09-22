#!/usr/bin/env python


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.listType = []
        self.setType = set()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if word in self.setType:
            return
        self.listType.append(word)
        self.setType.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # 针对流氓数据做流氓优化
        if word == '.':
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch in self.setType:
                    return True
            return False
        if not '.' in word:
            return word in self.setType
        possible = set()
        strlen = len(word)
        for possib in self.listType:
            if len(possib) == strlen:
                possible.add(possib)
        counter = 0
        for c in word:
            totaine = set()
            for filt in possible:
                if c != '.' and filt[counter] != c:
                    totaine.add(filt)
            possible -= totaine
            counter += 1
        return len(list(possible)) != 0

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
