#!/usr/bin/env python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, node: ListNode, k: int) -> List[ListNode]:
        if not node:
            return [None] * k
        
        raw_nodes = []
        
        while node:
            raw_nodes.append(node)
            node = node.next
        
        node_count = len(raw_nodes)
        
        base_count = node_count // k
        modula = node_count % k
        
        results = []

        
        previous = 0
        
        for i in range(k):
            cnt = base_count
            if i < modula:
                cnt += 1
                
            if cnt == 0:
                results.append(None)
            else:
                results.append(raw_nodes[previous])
                raw_nodes[previous + cnt - 1].next = None
                
            previous += cnt
            
        return results