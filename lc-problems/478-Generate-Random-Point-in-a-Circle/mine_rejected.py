#!/usr/bin/env python


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self) -> List[float]:
        rand_theta = random.random() * math.pi * 2
        rand_radius = random.random() * self.radius
        return [self.xc + rand_radius * math.cos(rand_theta), self.yc + rand_radius * math.sin(rand_theta)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
