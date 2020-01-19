#!/usr/bin/env python


class Solution:
    def findKthNumber(self, n, k):
        pre = 1  # 起始前缀
        pos = 1
        while pos < k:
            cnt = self.count(pre, n)
            if pos+cnt > k:
                # 在pre前缀下，在pre前缀对应的区间里pre，pos逐位移动
                pre *= 10
                pos += 1
            else:
                # next prefix
                pre += 1
                pos += cnt
        return pre

    # 以pre为前缀的数字个数
    def count(self, pre, n):
        # 以pre为前缀的数字在区间[a, min(n+1,b))，注意区间左闭右开,
        # 也就是如果b更小，则不能包含下一个前缀，如果n+1更小，则不能包含n+1(n为上界)
        cnt = 0
        a = pre
        b = pre+1
        while a <= n:
            cnt += min(n+1, b) - a  # 左闭右开，所以不会额外+1
            # update next a,b
            a *= 10
            b *= 10
        return cnt
