#!/usr/bin/env python


class Solution:
    def floodFillHelper(self, image, sr, sc, newColor, oldColor, visited):
        if not (0 <= sr < len(image) and 0 <= sc < len(image[0])) or visited[sr][sc] or image[sr][sc] != oldColor:
            return image
        image[sr][sc], visited[sr][sc], offsets = newColor, True, [
            [-1, 0], [1, 0], [0, -1], [0, 1]]
        for off in offsets:
            image = self.floodFillHelper(
                image, sr + off[0], sc + off[1], newColor, oldColor, visited)
        return image

    def floodFill(self, image, sr, sc, newColor):
        visited, old_color = [[0] * len(image[0])
                              for _ in range(len(image))], image[sr][sc]
        return self.floodFillHelper(image, sr, sc, newColor, old_color, visited)
