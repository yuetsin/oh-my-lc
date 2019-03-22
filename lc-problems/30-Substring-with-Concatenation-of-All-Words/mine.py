class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        slen = len(s)
        if len(words) < 1:
            return []

        each_word_len = len(words[0])

        ptr = 0

        rst = []

        limit = slen - each_word_len * len(words)
        while ptr <= limit:

            word = copy.deepcopy(words)

            lp = ptr

            while lp <= slen:
                if len(word) == 0:
                    rst.append(ptr)
                    break
                try:
                    word.remove(s[lp: lp + each_word_len])
                except:
                    break
                lp += each_word_len
            ptr += 1
        return rst
