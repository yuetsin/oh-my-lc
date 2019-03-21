class Solution:

    def addOnePair(self, str) -> set:
        rst_set = set()
        for i in range(len(str)):
            rst_set.add(str[:i] + '()' + str[i:])
        return rst_set

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        else:
            my_rst = set()
            for lst in self.generateParenthesis(n - 1):
                my_rst = my_rst.union(self.addOnePair(lst))

            return list(my_rst)
