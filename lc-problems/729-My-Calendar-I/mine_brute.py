#!/usr/bin/env python


class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:

        for event in self.events:
            if event[0] < end and event[1] > start:
                return False

        self.events.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
