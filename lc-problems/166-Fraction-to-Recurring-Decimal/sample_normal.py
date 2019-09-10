#!/usr/bin/env python


def fractionToDecimal(self, numerator, denominator):
    if numerator % denominator == 0:
        return str(numerator // denominator)
    p, q = map(abs, (numerator, denominator))
    prefix = ('' if (numerator > 0) == (denominator > 0) else '-') + \
        str(p // q) + '.'  # everything before the decimal point
    suffix = ''  # everything after the decimal point
    remainder = p % q
    index = {}
    while remainder not in index:  # search for recurrence
        index[remainder] = len(suffix)
        suffix += str(remainder * 10 // q)
        remainder = remainder * 10 % q
        if remainder == 0:
            return prefix + suffix  # no recurring decimal
    return prefix + suffix[:index[remainder]] + '(' + suffix[index[remainder]:] + ')'
