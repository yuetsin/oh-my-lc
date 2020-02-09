#!/usr/bin/env python


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # 你说什么 Beautiful 什么就 Beautiful 嘛？
        ans = list(range(1, n - k))
        for i in range(k + 1):
            if i % 2 == 0:
                ans.append(n - k + i // 2)
            else:
                ans.append(n - i // 2)

        return ans
