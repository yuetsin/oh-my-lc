class Solution:
    ptr = 0

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def getOne(words: List[str], maxWidth: int) -> str:
            thisLine = []
            currentLen = 0
            while self.ptr < len(words):
                if currentLen + len(thisLine) + len(words[self.ptr]) <= maxWidth:
                    thisLine.append(words[self.ptr])
                    currentLen += len(words[self.ptr])
                    self.ptr += 1
                else:
                    break
            if self.ptr == len(words):
                if thisLine != []:
                    return ' '.join(thisLine) + (maxWidth - currentLen - len(thisLine) + 1) * ' '
                else:
                    return
            else:
                if len(thisLine) == 1:
                    return thisLine[0] + (maxWidth - len(thisLine[0])) * ' '
                spaces = maxWidth - currentLen
                base = int(spaces / (len(thisLine) - 1))
                preprivilege = spaces - base * (len(thisLine) - 1)

                string = ""
                if thisLine == []:
                    return None
                for i in range(len(thisLine) - 1):
                    if i < preprivilege:
                        string += (thisLine[i] + ' ' * (base + 1))
                    else:
                        string += (thisLine[i] + ' ' * base)
                string += thisLine[-1]
                return string

        rst = []
        s = getOne(words, maxWidth)
        while s != None:
            rst.append(s)
            s = getOne(words, maxWidth)
        return rst
