#!/usr/bin/env python


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # 啊…看着全大写，没有下标的化学式好难受…

        def parse(string: str) -> dict:
            count = {}

            # elm = []
            # count = []

            pairs = []

            # True: alpha
            # False: numeric
            state = False

            rng = range(len(string))

            lens = len(string)
            i = 0
            while i < lens:
                # for i in range(len(string)):
                ch = string[i]
                if ch in '1234567890':
                    if state:
                        pairs[-1][1] = int(ch)
                    else:
                        pairs[-1][1] *= 10
                        pairs[-1][1] += int(ch)
                    state = False
                elif ch == '(':
                    depth = 0
                    for j in range(i, len(string)):
                        if string[j] == '(':
                            depth += 1
                        elif string[j] == ')':
                            depth -= 1
                            if depth == 0:
                                break

                    subdict = parse(string[i + 1: j])
                    pairs.append([subdict, 1])
                    # for k, v in subdict.items():
                    #     if k in count:
                    #         count[k] += v
                    #     else:
                    #         count.update({
                    #             k: v
                    #         })
                    i = j + 1
                    state = True
                    continue
                else:
                    if state and ch.islower():
                        pairs[-1][0] += ch
                    else:
                        pairs.append([ch, 1])
                    state = True
                i += 1
            # print(pairs)

            return pairs

        midexp = parse(formula)

        result = {}

        def flatten(elms, scale: int):
            for elm in elms:
                if type(elm[0]) == str:
                    if not elm[0] in result:
                        result.update({elm[0]: scale * elm[1]})
                    else:
                        result[elm[0]] += scale * elm[1]
                else:
                    flatten(elm[0], scale * elm[1])

        flatten(midexp, 1)

        final = []
        for k, v in sorted(result.items(), key=lambda x: x[0]):
            if v > 1:
                final.append('%s%d' % (k, v))
            else:
                final.append(k)

        return ''.join(final)
