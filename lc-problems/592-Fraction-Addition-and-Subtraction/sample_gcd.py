#!/usr/bin/env python


class Solution:
    def fractionAddition(self, expression: str) -> str:
        l, ll, b, flag = [], [], [], False

        import math

        for i in expression:
            if i.isdigit():
                b.append(i)

            elif i == '+' or i == '-':
                ll.append(''.join(b))
                b.clear()

                if i == '-':
                    b.append('-')

                if flag:
                    l.append(ll.copy())
                    ll.clear()
                    flag = False

            else:
                ll.append(''.join(b))
                b.clear()
                flag = True

        ll.append(''.join(b))
        l.append(ll.copy())

        num = int(l[0][-2])
        den = int(l[0][-1])

        for i in range(1, len(l)):
            num, den = int(l[i][1]) * num + den * \
                int(l[i][0]), den * int(l[i][1])

        if num == 0:
            return '0/1'

        if den == 1:
            return str(num) + '/1'

        gcd = math.gcd(num, den)

        return str(num // gcd) + '/' + str(den // gcd)
