#!/usr/bin/env python


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        yMax = len(board)
        xMax = len(board[0]) if yMax != 0 else 0

        def findFrom(x: int, y: int, wordIndex: int, since: int) -> bool:
            if since == len(words[wordIndex]):
                return True
            char = words[wordIndex][since]
            if x < 0 or x >= xMax:
                return False
            if y < 0 or y >= yMax:
                return False
            if not board[y][x] == char:
                return False

            board[y][x] = ''

            if findFrom(x, y + 1, wordIndex, since + 1):
                board[y][x] = char
                return True
            elif findFrom(x, y - 1, wordIndex, since + 1):
                board[y][x] = char
                return True
            elif findFrom(x - 1, y, wordIndex, since + 1):
                board[y][x] = char
                return True
            elif findFrom(x + 1, y, wordIndex, since + 1):
                board[y][x] = char
                return True
            else:
                board[y][x] = char
                return False

        foundWords = []
        for i in range(len(words)):
            firstChar = words[i][0]
            try:
                for xs in range(xMax):
                    for ys in range(yMax):
                        if board[ys][xs] == firstChar:
                            if findFrom(xs, ys, i, 0):
                                raise TypeError
            except:
                foundWords.append(words[i])
        return foundWords
