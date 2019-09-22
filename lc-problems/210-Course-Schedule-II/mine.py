#!/usr/bin/env python


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        unlearned = list(range(numCourses))
        sequence = []

        states = set()
        while len(unlearned) != 0:
            # print("current state: ", unlearned)
            if tuple(unlearned) in states:
                return []

            states.add(tuple(unlearned))
            tolearn = unlearned[0]

            unsatisfied_reqs = []
            for req in prerequisites:
                if req[0] == tolearn and req[1] in unlearned:
                    unsatisfied_reqs.append(req[1])
                    unlearned.remove(req[1])
            # print("unsatisfied: ", unsatisfied_reqs)
            if len(unsatisfied_reqs) == 0:
                sequence.append(tolearn)
                unlearned.remove(tolearn)
            else:
                # unlearned.remove(tolearn)
                # unlearned.append(tolearn)
                unlearned = unsatisfied_reqs + unlearned

        return sequence
