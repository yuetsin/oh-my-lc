#!/usr/bin/env python

class Solution:
    def isGoodGasPath(self, pure_cost: List[int]) -> bool:
        gas_left = 0
        for j in range(len(pure_cost)):
            gas_left += pure_cost[j]
            if gas_left < 0:
                return False
        return True
                    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        pure_cost = [gas[i] - cost[i] for i in range(len(gas))]
        length = len(pure_cost)
        if sum(pure_cost) < 0:
            return -1
        for i in range(length):
            if i == 0:
                new_lst = pure_cost
            else:
                new_lst = pure_cost[i:] + pure_cost[:i]
            if self.isGoodGasPath(new_lst):
                return i
        return -1
            