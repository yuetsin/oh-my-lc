#!/usr/bin/env python

"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

from functools import lru_cache


class Solution:
    def getImportance(self, employees: List['Employee'], idx: int) -> int:

        mmap = {}
        for emp in employees:
            mmap.update({
                emp.id: emp
            })

        @lru_cache(maxsize=None)
        def getImp(eid: int) -> int:
            employee = mmap[eid]
            importance = employee.importance
            for sub in employee.subordinates:
                importance += getImp(sub)
            return importance

        return getImp(idx)
