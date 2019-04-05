class Solution:

    def minWindow(self, s: str, t: str) -> str:

        length = len(s)
        tlen = len(t)

        def contain(s: str, t: str) -> bool:
            s = list(s)
            for ch in t:
                try:
                    idx = s.index(ch)
                    del s[idx]
                except:
                    return False
            return True
        cur_len = tlen
        if not contain(s, t):
            return ""

        while cur_len <= length:
            this_success = set()
            # print("curLen = %d" % cur_len)
            for i in range(length - cur_len + 1):
                if contain(s[i: i + cur_len], t):
                    # print("found str. %s" % substr[i : i + cur_len])
                    this_success.add(s[i: i + cur_len])
                    break
            if len(this_success) == 0:
                cur_len += 1
            else:
                for i in this_success:
                    return i
