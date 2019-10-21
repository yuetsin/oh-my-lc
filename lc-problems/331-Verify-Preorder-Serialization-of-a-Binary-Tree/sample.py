#!/usr/bin/env python


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        N = len(preorder)
        cnt = 0
        for i in range(N-1, -1, -1):
            if preorder[i] == '#':
                cnt += 1
            else:
                if cnt <= 1:
                    return False
                cnt -= 1
        return cnt == 1
