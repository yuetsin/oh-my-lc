class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def isValid(s: str):
            stack = []
            for char in s:
                if char == ')':
                    top_element = stack.pop() if stack else '#'
                    if top_element != '(':
                        return False
                else:
                    stack.append(char)
            return not stack
            
        strlen = len(s)
        curlen = strlen - 1 if strlen % 2 == 1 else strlen
        
        while curlen > 0:
            # print("curlen = %d" % curlen)
            # print("range: %d" % (strlen - curlen + 1))
            for i in range(strlen - curlen + 1):
                # print("     i = %d" % i)
                # print("check %s" % s[i : i + curlen])
                if isValid(s[i: i + curlen]):
                    return curlen
            curlen -= 2
        return 0