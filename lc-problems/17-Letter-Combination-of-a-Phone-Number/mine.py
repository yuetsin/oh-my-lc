class Solution:
    magic_nums = ['', '', 'abc', 'def', 'ghi',
                  'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def append_possibility(self, lst: List[str], num: int) -> List[str]:
        rst = []
        for s in self.magic_nums[num]:
            for itm in lst:
                rst.append(itm + s)
        return rst

    def letterCombinations(self, digits: str) -> List[str]:
        nums = [int(char) for char in list(digits)]

        rst = ['']
        for n in nums:
            rst = self.append_possibility(rst, n)

        return rst if rst != [''] else []
