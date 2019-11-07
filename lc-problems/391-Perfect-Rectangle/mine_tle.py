#!/usr/bin/env python


class Solution:
    overlapped = False

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        def tryCombine(idx1, idx2):
            rect1 = rectangles[idx1]
            rect2 = rectangles[idx2]
            if rect1[0] == rect2[0] and rect1[2] == rect2[2]:
                if rect1[3] == rect2[1]:
                    return [rect1[0], rect1[1], rect2[2], rect2[3]]
                elif rect2[3] == rect1[1]:
                    return [rect2[0], rect2[1], rect1[2], rect1[3]]

            elif rect1[1] == rect2[1] and rect1[3] == rect2[3]:
                if rect1[2] == rect2[0]:
                    return [rect1[0], rect1[1], rect2[2], rect2[3]]
                elif rect1[0] == rect2[2]:
                    return [rect2[0], rect2[1], rect1[2], rect1[3]]

        while len(rectangles) > 1:
            if overlapped:
                return False
            # print(rectangles)
            recC = len(rectangles)
            # print("recC:", recC)
            try:
                for reci1 in range(recC):
                    for reci2 in range(reci1 + 1, recC):
                        cb = tryCombine(reci1, reci2)
                        if cb:
                            # print("combined ", reci1, reci2)
                            rectangles.pop(reci2)
                            rectangles.pop(reci1)
                            rectangles.append(cb)
                            raise TypeError("Hooray!")
            except:
                continue

            return False

        if len(rectangles) == 0:
            return False
        return True
