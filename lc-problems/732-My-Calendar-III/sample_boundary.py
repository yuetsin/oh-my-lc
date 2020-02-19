#!/usr/bin/env python


class MyCalendarThree:

    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start, end):
        self.delta[start] += 1
        self.delta[end] -= 1

        active = ans = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            if active > ans:
                ans = active

        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
