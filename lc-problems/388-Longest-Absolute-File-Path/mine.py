#!/usr/bin/env python


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        if len(self.name) < 2:
            self.isFile = False
        elif '.' in self.name[:-1]:
            self.isFile = True
        else:
            self.isFile = False

    def longest(self) -> int:

        memax = len(self.name)

        if self.isFile:
            maxl = memax
        else:
            maxl = None

        for l in self.children:
            nextl = l.longest()
            if nextl:
                if maxl:
                    maxl = max(maxl, memax + nextl + 1)
                else:
                    maxl = len(self.name) + nextl + 1
        return maxl

    def printMe(self, indent=0):
        print('  ' * indent, self.name, "children count: ", len(self.children))
        for ch in self.children:
            ch.printMe(indent + 1)


class Solution:
    def lengthLongestPath(self, ins: str) -> int:
        lines = list(filter(None, ins.split('\n')))
        if not len(lines):
            return 0
        stacks = [Node('')]
        for line in lines:
            indentCount = line.count('\t')
            newNode = Node(line.replace('\t', ''))
            # print("indC:", indentCount)
            if indentCount + 2 > len(stacks):
                # print("insert children to", stacks[-1].name)
                stacks[-1].children.append(newNode)
                stacks.append(newNode)
            else:
                # print("insert children to", stacks[indentCount].name)
                stacks[indentCount].children.append(newNode)
                stacks = stacks[:indentCount + 1]
                stacks.append(newNode)
        # stacks[0].printMe()
        rs = stacks[0].longest()
        return rs - 1 if rs else 0
