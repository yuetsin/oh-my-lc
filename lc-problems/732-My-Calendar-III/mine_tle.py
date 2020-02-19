#!/usr/bin/env python

class MyCalendarThree:

    def __init__(self):
        self.tuples = []
        self.max_k = 0

    def book(self, start: int, end: int) -> int:
        self.tuples.append((start, end))
        
        maxx = 0
        
        for startp, _ in self.tuples:
            count = 0
            checkpoint = startp
            for tup in self.tuples:
                if checkpoint >= tup[0] and checkpoint < tup[1]:
                    count += 1
            maxx = max(maxx, count)
        
        for _, endp in self.tuples:
            count = 0
            checkpoint = endp
            for tup in self.tuples:
                if checkpoint >= tup[0] and checkpoint < tup[1]:
                    count += 1
            maxx = max(maxx, count)
        
        return maxx


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)