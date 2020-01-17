#!/usr/bin/env python


class Solution:
    def findMaximumXOR_trie(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2

        answer, root = 0, {}
        for n in nums:
            result = 0
            xor_node = cur = root

            for i in range(L - 1, -1, -1):
                bit = (n >> i) & 1
                # 这部分是建造树
                if bit not in cur:
                    cur[bit] = {}
                cur = cur[bit]

                if 1 - bit in xor_node:
                    result = (result << 1) + 1
                    xor_node = xor_node[1 - bit]
                else:
                    result = result << 1
                    xor_node = xor_node[bit]

            answer = max(answer, result)

        return answer

    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2

        answer = 0
        for i in range(L - 1, -1, -1):
            answer <<= 1
            current = answer + 1

            prefixes = set()
            for n in nums:
                temp = n >> i
                if temp ^ current in prefixes:
                    answer += 1
                    break

                prefixes.add(temp)

        return answer
