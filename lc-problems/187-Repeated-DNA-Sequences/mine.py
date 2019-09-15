class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        self.prec = set()
        self.result = set()
        strlen = len(s)
        if strlen <= 10:
            return []
        for i in range(0, strlen - 9):
            slicestr = s[i: i + 10]
            # print("checking", slicestr)
            if slicestr in self.prec:
                self.result.add(slicestr)
            else:
                self.prec.add(slicestr)
        return list(self.result)
