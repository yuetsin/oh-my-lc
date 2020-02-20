#!/usr/bin/env python


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        current_color = image[sr][sc]

        if current_color == newColor:
            return image

        ymax = len(image)
        xmax = len(image[0])

        def flow(x: int, y: int):
            image[y][x] = newColor

            if x > 0 and image[y][x - 1] == current_color:
                flow(x - 1, y)

            if x < xmax - 1 and image[y][x + 1] == current_color:
                flow(x + 1, y)

            if y > 0 and image[y - 1][x] == current_color:
                flow(x, y - 1)

            if y < ymax - 1 and image[y + 1][x] == current_color:
                flow(x, y + 1)

        flow(sc, sr)
        return image
