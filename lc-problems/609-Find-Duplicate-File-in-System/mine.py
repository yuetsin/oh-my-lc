#!/usr/bin/env python


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        mmap = {}
        for path in paths:
            comp = path.split(' ')
            rootp = comp[0]
            for file in comp[1:]:
                subcomp = file.split('(')
                filename = rootp + '/' + subcomp[0]
                content = subcomp[1][:-1]
                if content in mmap:
                    mmap[content].append(filename)
                else:
                    mmap.update({
                        content: [filename]
                    })

        rs = []
        for k, v in mmap.items():
            if len(v) > 1:
                rs.append(v)
        return rs
