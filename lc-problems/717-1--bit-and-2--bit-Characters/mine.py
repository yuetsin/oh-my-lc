#!/usr/bin/env python


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        bitcount = len(bits)

        # 0 - can be and only be decode as 1-bit
        def decode(since: int) -> bool:
            if since > bitcount - 1:
                return False
            elif since == bitcount - 1:
                return bits[since] == 0
            else:
                if bits[since] == 0:
                    return decode(since + 1)
                else:
                    return decode(since + 2)

        return decode(0)
