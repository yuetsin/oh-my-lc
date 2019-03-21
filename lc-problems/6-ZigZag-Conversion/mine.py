class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rsts = ''
        strlen = len(s)
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                leap = 2 * (numRows - 1)
                str_itr = i
                while str_itr < strlen:
                    rsts += s[str_itr]
                    str_itr += leap

            else:
                leapA = 2 * (numRows - i - 1)
                leapB = 2 * i

                str_itr = i
                while str_itr < strlen:
                    rsts += s[str_itr]
                    str_itr += leapA

                    if str_itr < strlen:
                        rsts += s[str_itr]
                        str_itr += leapB
                    else:
                        break
        return rsts
