#!/usr/bin/env python


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        z_os = []

        total_zeroes = 0
        total_ones = 0
        for string in strs:
            zero_count = string.count('0')
            one_count = len(string) - zero_count
            z_os.append((zero_count, one_count))
            total_zeroes += zero_count
            total_ones += one_count

        if total_zeroes <= m and total_ones <= n:
            # Full Combo!
            return len(strs)

        def dfs(m: int, n: int) -> int:
            if m == 0 and n == 0:
                return 0

            might_be = 0
            for target in z_os:
                if target[0] <= m and target[1] <= n:
                    z_os.remove(target)
                    might_be = max(
                        might_be, 1 + dfs(m - target[0], n - target[1]))
                    z_os.append(target)
            return might_be
        return dfs(m, n)
