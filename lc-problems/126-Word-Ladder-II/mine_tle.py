#!/usr/bin/env python3


def differ(s: str, t: str) -> int:
    if len(s) != len(t):
        return -1
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    return count


class Word:
    def __init__(self, word_str):
        self.word = word_str
        self.next = []

    def buildNext(self, word_list):
        for word in word_list:
            if differ(word.word, self.word) == 1:
                self.next.append(word)


class Solution:

    startWord = None

    visited = set()

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not endWord in wordList:
            return []
        wordDict = []
        for word in wordList:
            wordDict.append(Word(word))

        self.startWord = Word(beginWord)
        self.endWord = Word(endWord)

        wordDict.append(self.startWord)
        wordDict.append(self.endWord)

#         print([w.word for w in wordDict])
        for wordClass in wordDict:
            wordClass.buildNext(wordDict)

        possible_rst = []

        def getPath(since):
            this_rst = []
            # node = since
            if since != self.endWord:
                for i in since.next:
                    if not i in self.visited:
                        self.visited.add(since)
                        l = getPath(i)
                        # print(l)
                        self.visited.remove(since)
                        for rl in l:
                            this_rst.append([since] + rl)
            else:
                return [[self.endWord]]

            return this_rst

        real_rst = []
        for l in getPath(self.startWord):
            # print(l)
            real_rst.append([i.word for i in l])
        try:
            minlen = min([len(i) for i in real_rst])
        except:
            minlen = 2
        # print(minlen)
        realreal_rst = []
        for l in real_rst:
            if len(l) == minlen:
                flag = True
                for r in realreal_rst:
                    if r == l:
                        flag = False
                        break
                if flag:
                    realreal_rst.append(l)
        return realreal_rst
