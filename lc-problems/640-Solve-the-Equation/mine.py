class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')

        def parse(string: str) -> tuple:

            chrs = [-1]
            for chi in range(len(string)):
                ch = string[chi]
                if ch == '+' or ch == '-':
                    chrs.append(chi)

            chrs.append(len(string))
            tokens = []
            if len(chrs) == 0:
                tokens.append((string), True)
            else:
                for i in range(len(chrs) - 1):
                    if chrs[i] == -1:
                        sig = True
                    else:
                        # print(string[chrs[i]])
                        sig = string[chrs[i]] == '+'
                    tokens.append((string[chrs[i] + 1: chrs[i + 1]], sig))

            # print(tokens)

            k, c = 0, 0
            for v, sig in tokens:
                if v == '':
                    continue
                if sig:
                    if v == 'x':
                        k += 1
                    elif v[-1] == 'x':
                        k += int(v[:-1])
                    else:
                        c += int(v)
                else:
                    if v == 'x':
                        k -= 1
                    elif v[-1] == 'x':
                        k -= int(v[:-1])
                    else:
                        c -= int(v)

            return k, c

        k1, c1 = parse(left)
        k2, c2 = parse(right)

        # if k1 != k2 and c1 == c2:
        #     return 'x=0'

        if k1 == k2 and c1 != c2:
            return "No solution"

        if k1 == k2 and c1 == c2:
            return "Infinite solutions"

        return 'x=%d' % -((c2 - c1) // (k2 - k1))
