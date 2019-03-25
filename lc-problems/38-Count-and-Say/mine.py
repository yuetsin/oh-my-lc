class Solution:
    tmpLib = ['', '1', '11', '21', '1211', '111221']
    def countAndSay(self, n: int) -> str:
        
        if n < 6:
            return self.tmpLib[n]
        last = self.countAndSay(n - 1)
        
        new_str = ''
        ptr = 0
        strlen = len(last)
        
        cont_str = ''
        while ptr < strlen:
            if ptr == 0 or last[ptr] == last[ptr - 1]:
                cont_str += last[ptr]
                ptr += 1
                continue
            new_str += ("%d%s" % (len(cont_str), cont_str[0]))
            cont_str = last[ptr]
            ptr += 1
        if cont_str != "":
            new_str += ("%d%s" % (len(cont_str), cont_str[0]))
        return new_str