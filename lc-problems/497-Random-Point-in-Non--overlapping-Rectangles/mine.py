import random


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.areas = []
        self.rects = rects
        for rect in rects:
            self.areas.append((rect[2] + 1 - rect[0])
                              * (rect[3] + 1 - rect[1]))

    def pick(self) -> List[int]:
        rv = random.randint(1, sum(self.areas))
        counter = 0
        for area in self.areas:
            total += area
            if total >= rv:
                break
            counter += 1

        chosen_rect = self.rects[counter]

        # fallen into rect[counter]
        new_x = random.randint(chosen_rect[0], chosen_rect[2])
        new_y = random.randint(chosen_rect[1], chosen_rect[3])
        return [new_x, new_y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
