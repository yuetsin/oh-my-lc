class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        longest = 0
        stack.append(-1)
        idx = 0
        for ch in s:
            # print("Now, stack = %s" % str(stack))
            if ch == '(':
                stack.append(idx)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    longest = max(longest, idx - stack[-1])
            idx += 1

        return longest
