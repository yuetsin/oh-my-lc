#!/usr/bin/env python


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        cnt = len(nums)

        def singleDirection(since: int) -> bool:
            # print("==================")
            visited = set()
            last = None

            direction = None

            while True:
                if not since in visited:
                    visited.add(since)
                    last = since
                else:
                    break

                steps = nums[since]
                # print("check since = ", since, ", steps = ", steps)

                if direction == None:
                    if steps > 0:
                        direction = True
                    else:
                        direction = False
                elif direction == True and steps < 0:
                    return False
                elif direction == False and steps > 0:
                    return False

                since += steps
                while since < 0:
                    since += cnt

                while since >= cnt:
                    since -= cnt

            return last != since

        for i in range(cnt):
            if singleDirection(i):
                # print("Possibly", i)
                return True

        return False
