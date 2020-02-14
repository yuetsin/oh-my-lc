#!/usr/bin/env python


class Solution:

    mao_sun = '卯榫'

    def removeComments(self, source: List[str]) -> List[str]:

        commenting = False
        # False - normal going
        # True - it's under a multiline comments

        result = []

        for line in source:

            t1, t2, t3 = line.find('//'), line.find('/*'), line.find('*/')
            available_tokens = []

            for tok in [t1, t2, t3]:
                if tok != -1:
                    available_tokens.append(tok)

            if not available_tokens:
                if commenting:
                    result.append(line)
                continue

            min_token = min(available_tokens)

            if not commenting:

                if min_token == t1 and t1 > 0:
                    # first effective token is //
                    result.append(line[:t1])
                elif min_token == t2:
                    if t2 > 0:
                        result.append(line[:t2] + self.mao_sun)
                    commenting = True
            else:
                if min_token == t3:
                    if t3 + 2 < len(line):
                        result.append(self.mao_sun + line[t3 + 2:])
                    commenting = False

        return '\n'.join(result).replace('卯榫\n卯榫', '').split('\n')
