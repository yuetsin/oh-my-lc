#!/usr/bin/env python


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        if boxes == []:
            return 0

        def startRemove() -> int:
            # print(boxes)
            result = []
            for box in boxes:
                if result and result[-1][0] == box:
                    result[-1][1] += 1
                else:
                    result.append([box, 1])

            score = 0
            # print(result)

            index = 0
            for item in result:
                # before = copy.deepcopy(boxes)
                # if item[0] == item[1]:
                for _ in range(item[1]):
                    boxes.pop(index)
                score = max(score, item[1] * item[1] + startRemove())
                for _ in range(item[1]):
                    boxes.insert(index, item[0])
                # assert(before == boxes)
                index += item[1]

            return score
        return startRemove()
