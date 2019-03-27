class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aDict = {}
        for word in strs:
            tag = ''.join(sorted(list(word)))
            try:
                aDict[tag].append(word)
            except:
                aDict.update({tag: [word]})
        
        rst = []
        for a in aDict:
            rst.append(aDict[a])
        return rst