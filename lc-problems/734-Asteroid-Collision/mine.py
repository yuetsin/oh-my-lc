#!/usr/bin/env python


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        begins = 0
        while True:
            # print(begins)
            exploded = False
            found = False
            for i in range(begins, len(asteroids)):
                if found:
                    break

                asteroid = asteroids[i]

                if asteroid < 0:
                    for j in range(i - 1, -1, -1):
                        if asteroids[j] > 0:
                            exploded = True
                            if asteroids[j] > -asteroid:
                                del asteroids[i]
                            elif asteroids[j] < -asteroid:
                                del asteroids[j]
                            else:
                                del asteroids[i]
                                del asteroids[j]
                            found = True
                            break
            if not exploded:
                begins += 1
            if begins >= len(asteroids) - 1:
                break

        return asteroids
