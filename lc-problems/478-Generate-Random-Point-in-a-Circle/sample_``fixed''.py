#!/usr/bin/env python


class Solution(object):

    def __init__(self, radius, x_center, y_center):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        r = (self.randomize(0, math.pi * self.r ** 2) / math.pi) ** 0.5
        theta = self.randomize(0, 2 * math.pi)
        return [self.x + r * math.cos(theta), self.y + r * math.sin(theta)]

    def randomize(self, a, b):
        return random.uniform(a, b)
