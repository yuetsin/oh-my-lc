#!/usr/bin/env python


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        if nodes == []:
            return True

        def traverse():
            if not nodes:
                raise TypeError("")
            head = nodes.pop(0)
            if head != '#':
                traverse()
                traverse()

        try:
            traverse()
        except:
            return False

        return nodes == []
